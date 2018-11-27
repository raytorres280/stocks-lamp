current_time="`date +%Y-%m-%d-%H-%M-%S.html`"
echo "$current_time"

curl "http://wsj.com/mdc/public/page/2_3021-activnnm-actives.html" -o $current_time



soup_dom=`java -jar tagsoup-1.2.1.jar --files $current_time`

python3 parse-dom.py


# echo "$soup_dom"
echo hello
echo soup_dom
echo world
# echo $soup_dom
#for i in 60 (hour)
#get data,
#add to csv
#wait 60 seconds


