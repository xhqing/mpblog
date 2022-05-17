# 克隆自聚宽文章：https://www.joinquant.com/post/804
# 标题：基于主成分分析的量化选股策略
# 作者：Alphamon

import numpy as np
import pandas as pd
from scipy.stats import zscore

def pca(inVector,method = 'topNfactor',threshold = 9999999):
    # 数据标准化（均值标准化），消除量纲影响
    meanVals = np.mean(inVector,axis = 0)
    meanShift = inVector - meanVals
    # normVector = meanShift
    normVector = zscore(inVector,axis = 0)
    
    # 求协方差
    covMat = np.cov(normVector,rowvar = 0)

    # 求特征值和特征向量
    eigVals,eigVects = np.linalg.eig(mat(covMat))

    # 求解主成分的方差信息贡献率
    infoCtri = eigVals / np.sum(eigVals)

    # 对特征值排序,取索引值
    eigValInd = np.argsort(-eigVals)

    # 选择N主成分
    if method == 'topNfactor':
        # 求topN个特征值
        eigValInd = eigValInd[:threshold+1]
    elif method == 'totalVarThre':
        # 取累积解释量达到累积方差贡献率阈值的主成分
        lenEigValInd = len(eigValInd)
        sumVarCtri = np.sum(infoCtri)
        for i in range(lenEigValInd):
        	if np.sum(infoCtri[eigValInd[:i+1]]) / sumVarCtri > threshold:
        		break
        	else:
        		continue
        eigValInd = np.array(eigValInd[:i+1])
        # print(eigVals,infoCtri,eigValInd)
    else:
        return "请输入合法的方法：topNfactor或者totalVarThre."
    # 取满足条件对应的特征向量和特征值
    redEigVects = eigVects[:,eigValInd]
    redEigVals = eigVals[eigValInd]
    infoCtri = np.mat(redEigVals / np.sum(redEigVals))
    sumVarCtri = np.sum(infoCtri)

    # 降维到N维
    nDimVector = normVector * redEigVects

    # 降维后的数据分布
    reconMat = (nDimVector * redEigVects.T) + meanVals

    # 求解综合绩效
    comPerformMat = (nDimVector * infoCtri.T) / sumVarCtri
    return nDimVector,reconMat,comPerformMat
    
def initialize(context):
    # 定义一个全局变量, 保存要操作的股票
    # 本策略仅选取上证指数的股票
    stocks1 = get_index_stocks('000001.XSHG')
    stocks2 = get_index_stocks('399001.XSHE')
    g.stocks = stocks1 + stocks2
    
    # 初始化此策略
    # 设置我们要操作的股票池, 这里我们只操作一支股票
    set_universe(g.stocks)
    
    # 购买标记，如果已经购买过该股票则不再购买该股票
    g.buyStocks = {}

# 每个单位时间(本策略建议按天调用)调用一次
def handle_data(context, data):
    stocks = g.stocks
    # 获取当前时间
    today = context.current_dt.strftime("%Y-%m-%d")
    #today = '2015-10-12'
    # 获取股票的财务指标数据
    df = get_fundamentals(query(
        valuation,balance,cash_flow,income
        ).filter(
        valuation.code.in_(stocks)
        ), date = today)
    # 获取可用的行列,删除无用的day\pubdate\statedate\id\code
    df = df.drop(['id','id.1','id.2','id.3','day','day.1','day.2','day.3','code.1','code.2','code.3','pubDate','statDate','pubDate.1','statDate.1','pubDate.2','statDate.2'],axis = 1)
    
    # 数据预处理，用均值代替NAN值和INF值
    #df = df.fillna(df.mean()) #也可以用均值代替，但是需要注意某一指标全为0的情况
    df = df.fillna(0) # 可以用任意数字代替
    
    # 生成待处理的矩阵
    dataVect = mat(df.drop(['code'],axis = 1))
    
    # PCA
    #topN = 10
    varThre = 0.8
    nDimVec,reconMat,comPerformMat = pca(dataVect,'totalVarThre',varThre)
    
    # 根据综合绩效值降序排序
    candidateStocks = {'code':list(df['code']),'performance':list(comPerformMat)}
    candidateStocks = pd.DataFrame(candidateStocks)
    candidateStocks.sort_index(by = 'performance',ascending = False)
    
    # 取topM只股票形成股票池（前5绩效的股票）
    #topM = floor(0.3 * len(df))
    topM = 8
    candidateStocks = candidateStocks[:topM]
    candidateStocks = list(candidateStocks['code'])
    
    # 循环已持有股票
    for security in context.portfolio.positions.keys():
        # 判断当前是否持有目前股票
        if security in candidateStocks:
            # 如果已持有股票在新的候选池里则继续持有，否则卖出
            continue
        else:
            # 全部卖出
            order_target(security,0)
            # 记录本次卖出
            print("Selling %s" %(security))
    # 循环股票池
    for security in candidateStocks:
        # 判断是否持有该股票以及是否有现金购买
        if security not in g.buyStocks and not data[security].paused:
            # 计算持仓量
            cash = context.portfolio.cash
            cash = cash / topM
            currentPrice = data[security].price
            cash = cash / currentPrice
            # 下入买入单
            order_target(security,cash)
            # 标记该股票
            g.buyStocks[security] = 1
            # 记录本次买入
            print("Buying %s" %(security))
        else:
            continue
