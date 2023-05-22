import psycopg2

def djselect():
    connection = psycopg2.connect(host='localhost', dbname='FHWDB', user='postgres', password='Q1w2e3r4')
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM public.parse ORDER BY id;''')
    arr = list(cursor.fetchall())
    res = ''
    k = 0
    while k != len(arr):
        i = arr[k]
        res = res + f'''<div class="grid__item shoes">
    				<div class="slider">
    					<div class="slider__item"><img src="/static/polls/images/PFDB{k}.jpg" alt="Dummy" /></div>
    				</div>
    				<div class="meta">
    					<h3 class="meta__title">{i[1]}</h3>
    					<span class="meta__brand">Скидка: {i[3]}</span>
    					<span class="meta__price">{i[2]}</span>
    				</div>
    				<button class="action action--button action--buy"><i class="fa fa-shopping-cart"></i><span class="text-hidden">Add to cart</span></button>
    			</div>
            '''
        k += 1

    cursor.close()
    connection.close()
    return res
