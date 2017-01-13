grep ">" $1 | cut -d " " -f3 | sort | uniq -c > $(echo $1 | cut -d'_' -f 1).count.txt
