# Overview

This charm provides [GitLab Runner](https://docs.gitlab.com/runner/).

GitLab Runner is the open source project that is used to run your jobs and
send the results back to GitLab. It is used in conjunction with GitLab CI,
the open-source continuous integration service included with GitLab that
coordinates the jobs.

# Usage

juju deploy gitlab-runner
juju config gitlab-runner registration-token=<token>

## Scale out Usage

Each unit of gitlab-runner will register with GitLab as a runner. You
can deploy separate gitlab-runner applications to scope runners to
specific projects.

# Configuration

TODO: registration-token

