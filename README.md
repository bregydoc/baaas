```bash
docker run -p 9222:9222 -e CHROME_OPTS='--disable-dev-shm-usage --force-gpu-mem-available-mb --full
-memory-crash-report' alpeware/chrome-headless-stable:ver-83.0.4103.61
```

```bash
go run github.com/MontFerret/ferret scrapper.aql
```
