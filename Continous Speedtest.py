import time
import speedtest

while True:
    # Use Speedtest CLI to get the results
    results = speedtest.Speedtest()
    results.get_best_server()
    download = results.download()
    upload = results.upload()
    ping = results.results.ping

    # Write the results to a CSV file
    with open('speedtest_results.csv', 'a') as f:
        f.write(f"{time.time()}, {download}, {upload}, {ping}\n")
    
    # Wait two minutes before running again
    time.sleep(120)