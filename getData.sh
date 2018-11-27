


#do 60 times, with 60 second wait at start of loop.

counter=0
while [ $counter -lt 60 ]
do
echo $counter

sleep 60

current_time=`date +%Y-%m-%d-%H-%M-%S`

curl "http://wsj.com/mdc/public/page/2_3021-activnnm-actives.html" -o ${current_time}.html

soup_dom=`java -jar tagsoup-1.2.1.jar --files $current_time.html`

python3 parse-dom.py ${current_time}.xhtml

((counter++))
done