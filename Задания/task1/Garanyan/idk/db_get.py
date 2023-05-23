import psycopg2

def djselect():
    connection = psycopg2.connect(host='localhost', dbname='dbdata', user='postgres', password='Q1w2e3r4')
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM public.food''')
    arr = list(cursor.fetchall())
    res = ''
    k = 0
    while k != len(arr):
        i = arr[k]
        res = res + f'''<div class="col-xl-6 col-md-6 col-lg-6">
    				<div class="single_delicious d-flex align-items-center">
                        <div class="thumb">
                            <img src="/static/polls/images/food{k}.jpg" alt="" /></div>
    				</div>
    				<div class="info">
    					<h3>{i[1]}</h3>
    					<span>{i[2]}</span>
    					<p></p>
    				</div>
                    </div>
                </div>'''
        k += 1

    cursor.close()
    connection.close()
    return res