name: Main - CI

on:
  push:
    branches: [ "main" ]

jobs:
  pipeline:
    uses: ./.github/workflows/ci-pipeline.yml
    with:
      run_push: false

