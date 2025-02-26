from com_stock_api.resources.member import Member, Members, Auth, Access, HighChurnMembers, MemberNameSearch
from com_stock_api.resources.board import Board, Boards, BoardTitleSearch
from com_stock_api.resources.comment import Comment, Comments, CommentMaxNum
from com_stock_api.resources.trading import Trading, Tradings, TradingRecommendStock

from com_stock_api.resources.yhfinance import YHFinance, YHFinances, TeslaGraph, AppleGraph
from com_stock_api.resources.recent_news import RecentNews, AppleNews, TeslaNews
from com_stock_api.resources.investingnews import Investing, AppleSentiment, TeslaSentiment
from com_stock_api.resources.nasdaq_prediction import NasdaqPrediction, NasdaqPredictions, PredGraph, PredGraph
from com_stock_api.resources.uscovid import USCovid, USCovids, USNewCases, CANewCases

from com_stock_api.resources.korea_covid import KoreaCovid,KoreaCovids
from com_stock_api.resources.kospi_pred import Kospi,Kospis,lgchem_pred,lginnotek_pred
from com_stock_api.resources.korea_finance import Stock,Stocks,lgchem,lginnotek
from com_stock_api.resources.korea_news import News,News_,Lgchem_Label,Lginnotek_Label
from com_stock_api.resources.korea_news_recent import RNews,RNews_, lgchemNews,lginnoteknews


from com_stock_api.resources.home import Home

def initialize_routes(api):
    print('=============== route.py')

    api.add_resource(Members, '/api/members')
    api.add_resource(Member, '/api/member', '/api/member/<string:email>')
    api.add_resource(Auth, '/api/auth')
    api.add_resource(Access, '/api/access')
    api.add_resource(HighChurnMembers, '/api/highchurnmembers')
    api.add_resource(MemberNameSearch, '/api/member-by-name/<string:name>')
    api.add_resource(Boards, '/api/boards')
    api.add_resource(Board, '/api/board', '/api/board/<string:id>')
    api.add_resource(BoardTitleSearch, '/api/board/<string:title>')
    api.add_resource(Comments, '/api/comments', '/api/comments/<string:id>')
    api.add_resource(Comment, '/api/comment', '/api/comment/<string:id>')
    api.add_resource(CommentMaxNum, '/api/commentmaxnum/<string:id>')
    api.add_resource(Tradings, '/api/tradings', '/api/tradings/<string:email>')
    api.add_resource(Trading, '/api/trading', '/api/trading/<string:id>')
    api.add_resource(TradingRecommendStock, '/api/trading-recommend/<string:email>')

    api.add_resource(NasdaqPredictions, '/nasdaq/predictions')
    api.add_resource(PredGraph, '/nasdaq/pred')
    api.add_resource(AppleGraph, '/nasdaq/apple')
    api.add_resource(TeslaGraph, '/nasdaq/tesla')
    api.add_resource(AppleNews, '/nasdaq/apple_news')
    api.add_resource(TeslaNews, '/nasdaq/tesla_news')
    api.add_resource(AppleSentiment, '/nasdaq/apple_sentiment')
    api.add_resource(TeslaSentiment, '/nasdaq/tesla_sentiment')
    api.add_resource(USCovid, '/nasdaq/uscovid')
    api.add_resource(USNewCases, '/nasdaq/us_new_cases')
    api.add_resource(CANewCases, '/nasdaq/ca_new_cases')

    api.add_resource(KoreaCovid,'/kospi/koreacovid')

    api.add_resource(lgchemNews,'/kospi/lgchemnews')
    api.add_resource(lginnoteknews,'/kospi/lginnoteknews')
    api.add_resource(Lgchem_Label, '/kospi/lgchem_label')
    api.add_resource(Lginnotek_Label, '/kospi/lginnotek_label')

    api.add_resource(lgchem,'/kospi/lgchem')
    api.add_resource(lginnotek,'/kospi/lginnotek')

    api.add_resource(lgchem_pred, '/kospi/lgchem_pred')
    api.add_resource(lginnotek_pred, '/kospi/lginnotek_pred')