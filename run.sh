HOST=0.0.0.0 PORT=9877 ./target/witd
curl -X GET "http://localhost:9877/start?autoend=true&access_token=<YOUR_ACCESS_TOKEN>" > witout.txt
./playMusic witout.txt