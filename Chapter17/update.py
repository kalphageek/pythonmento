import pymysql                                 # sqlite3 모듈 탑재
from Chapter17.select import select_title_book    # 데이터 조회용 함수 탑재


# 데이터 수정용 함수
def update_books():
    try:
        conn = pymysql.connect(host='localhost', port=13306, user='root', passwd='root', db='bookstore', charset='utf8',
                             autocommit=False)
        cur = conn.cursor()  # 커서 확보

        # 데이터 수정 SQL ( 제목이 %s 인 책의 추천 유무를 %s 로 변경하라 )
        update_sql = 'UPDATE books SET recommendation=%s WHERE title=%s'

        # 수정 SQL 실행
        cur.execute(update_sql, (1, '개발자의 코드'))

        conn.commit()                                   # 데이터베이스 반영
        print('데이터 수정 건수]', cur.rowcount)
        print('[데이터 수정 완료] ================== ')

    except:
        print ("예외 상황 발생")
        conn.rollback()                          # 데이터베이스 원복 (롤백)

    finally:
        conn.close()                                    # 커넥션 닫기

if __name__ == "__main__":		                # 외부에서 호출 시
    select_title_book('개발자의 코드')
    update_books()                                  # 데이터 수정 함수 호출
    select_title_book('개발자의 코드')
