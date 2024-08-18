replace all jpg files with webp files
`find ~/jpgram/jpgram/magazine/static/magazine/ -type f -name "*.jpg" -exec sh -c '~/libwebp-directory/libwebp-1.4.0-linux
-x86-64/bin/cwebp -q 40 "$1" -o "${1%.jpg}.webp" && rm "$1"' _ {} \;`

instaloader scrape new data
`cd ~/jpgram/jpgram/magazine/static/magazine/ && instaloader +args.txt`