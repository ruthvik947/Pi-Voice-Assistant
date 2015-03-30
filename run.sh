HOST=0.0.0.0 PORT=9877 ./target/witd
curl -X GET "http://localhost:9877/start?autoend=true&access_token=WYHWRTQSLPCBI2IKXS3JNKJIHVIRPV7M" > witout.json
python playMusic.py witout.json