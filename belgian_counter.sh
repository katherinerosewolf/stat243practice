grep -o Belgium cpds.csv > belgians.txt; wc -l belgians.txt

echo "There are $(grep -o Belgium cpds.csv | wc -l) occurrences of Belgium"

cut -d "," -f 4 RTADataSub.csv | sort | uniq | grep -E "[^0-9]"

for((i=1;i<=10;i++)); do 
    cut -d "," -f 4 RTADataSub.csv | sort | uniq | grep -E "[^0-9]"
done

# post challenge 2
touch downloads/test{1..4}

function mvlast() {
    mv "downloads/$(ls -rt \
       downloads | tail -n 1)" $1
}

cut -d',' -f6 cpds.csv | sort | head

tail -n +2 cpds.csv | cut -d',' -f6 | sort | head -n 1

# bash challenge 3
grep Belgium cpds.csv | cut -d',' -f6 | sort -n | head -n 1 

countries = $(cut -d"," -f2 cpds.csv | sed "s/\"//g" | sort | uniq)

grep -v x RTADataSub.csv > filtered_data.csv

# regex challenge solution
echo ${text} | sed -E "s/\",/\"|/g" | sed -E "s/,,/||/g

