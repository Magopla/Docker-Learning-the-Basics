# Section 5.1: Why Docker Fits CI/CD

CI/CD works best when builds are repeatable and environments behave predictably. Docker helps with both.

## Why Docker Helps

With Docker, a team can:

- package the application and dependencies together
- build the image once
- test that same image
- promote that same image to later environments

That reduces a common problem in delivery pipelines:

- local code works
- CI behaves differently
- deployment environment behaves differently again

## Build Once, Promote Many Times

One of the biggest advantages of Docker in CI/CD is that the artifact can stay stable across environments.

What usually changes between environments:

- environment variables
- secrets
- hostnames
- ports
- resource limits

What should ideally stay the same:

- the application image
- the application code inside it
- the tested dependencies

## Docker In A Sprint Workflow

A simple sprint delivery flow often looks like this:

1. Build the feature or fix locally.
2. Run the app in a local Docker environment.
3. Push the branch.
4. CI builds and tests the image.
5. CI deploys the image to a shared dev environment.
6. The team validates the sprint output.
7. The same image is promoted to production.

## Mini Quiz

1. Why is it useful to promote the same image rather than rebuild it for each environment?
2. Which kinds of values should change between environments without rebuilding the image?
3. Why does Docker help reduce "it worked in CI but not in production" problems?

## Next Step

Continue to [`02-environments-dev-to-production.md`](./02-environments-dev-to-production.md).
