#!/bin/bash

echo 'CTRL + C = STOP'
PS3='Masukan Pilihan : '
xnuvers007=("Manda Crack FB" "Manda Crack Instagram" "QUIT")
select xnuvers in "{xnuvers007[@]}"
do
        case $xnuvers in
                "Manda Crack FB")
                        python2 manda_crack.py;;
                "Manda Crack Instagram")
                        python2 menu_instagram.py;;
                "QUIT")
                        echo 'Tunggu 3 Detik akan keluar'
                        sleep 3
                        break;;
                *) echo "pilihan Tidak ada";;
        esac
done
