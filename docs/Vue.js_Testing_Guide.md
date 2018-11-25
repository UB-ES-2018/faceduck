# A 10-second guide to Vue.js frontend testing

Use this guides:
- https://vue-test-utils.vuejs.org/guides/#getting-started
- https://jestjs.io/docs/en/expect

Run tests from /faceduck with:
```bash
docker-compose run --entrypoint "npm run test:unit" frontend
```

Run coverage analysis from /faceduck with:
```bash
docker-compose run --entrypoint "npm run test:unit -- --coverage" frontend
```

In case of doubt, ask in Slack!
