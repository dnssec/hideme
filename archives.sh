#!/usr/bin/env bash
opt1="Launch HTTrack"
opt2="Launch WebHTTrack"
opt3="Launch ChangeDetection"
opt4="Internet Archive Tool"
opt5="Archive Box"
timestamp=$(date +%Y-%m-%d:%H:%M)
domainmenu=$(zenity  --list  --title "Archives Tool" --radiolist  --column "" --column "" TRUE "$opt1" FALSE "$opt2" FALSE "$opt3" FALSE "$opt4" FALSE "$opt5" --height=400 --width=300)
case $domainmenu in
$opt1 )
httrack
exit;;
$opt2 )
webhttrack
exit;;
$opt3 )
mkdir ~/Documents/ChangeDetection
changedetection.io -d ~/Documents/ChangeDetection -p 5000 & firefox http://127.0.0.1:5000
exit;;
$opt4 )
url=$(zenity --entry --title "Internet Archive Tool" --text "Enter Target URL")
mkdir ~/Documents/waybackpy
mkdir ~/Documents/waybackpy/$url
cd ~/Documents/waybackpy/$url
waybackpy --url "$url" --known_urls
waybackpy --url "$url" --oldest >> $url.txt
waybackpy --url "$url" --newest >> $url.txt
waybackpy --url "$url" --near --year 2010 >> $url.txt
waybackpy --url "$url" --near --year 2011 >> $url.txt
waybackpy --url "$url" --near --year 2012 >> $url.txt
waybackpy --url "$url" --near --year 2013 >> $url.txt
waybackpy --url "$url" --near --year 2014 >> $url.txt
waybackpy --url "$url" --near --year 2015 >> $url.txt
waybackpy --url "$url" --near --year 2016 >> $url.txt
waybackpy --url "$url" --near --year 2017 >> $url.txt
waybackpy --url "$url" --near --year 2018 >> $url.txt
waybackpy --url "$url" --near --year 2019 >> $url.txt
waybackpy --url "$url" --near --year 2020 >> $url.txt
waybackpy --url "$url" --near --year 2021 >> $url.txt
sort -u -i $url.txt -o $url.sorted.txt
webscreenshot -r chrome -q 100 -i $url.sorted.txt -w 1
waybackpy --url "$url" -o > oldest.html
waybackpy --url "$url" -n > newest.html
open ~/Documents/waybackpy/$url >/dev/null
exit;;
$opt5 )
url=$(zenity --entry --title "Archive Box" --text "Enter FULL Target URL")
cd ~/Documents/archivebox
archivebox add ''$url''
archivebox server 0.0.0.0:8000 &
sleep 3
firefox http://0.0.0.0:8000/
exit;;
esac


