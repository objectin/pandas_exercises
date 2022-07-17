import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

    # 여기에 로그 저장할 파일이름 넣기 : 전략이름
    strategy_name = 'buy'

    logger = logging.getLogger(strategy_name)
    logger.addHandler(logging.FileHandler(strategy_name + '.log'))
    
    print('')
    import datetime
    logger.info(f"매도 1번 : {'삼성전자'}, 매도시간: {datetime.datetime.now()}")
    logger.info(f"매도 1번 : {'셀트리온'}, 매도시간: {datetime.datetime.now()}")

'''
elif ( 수익률 > 12  or 수익률 <= self.vars[20] ):
    매도 = True
    logger.info(f"매도 3: {종목명}, 매도시간: {strf_time('%m%d %H%M%S', now())}")
'''
