<<<<<<< HEAD
# my_dagster_project

This is a [Dagster](https://dagster.io/) project scaffolded with [`dagster project scaffold`](https://docs.dagster.io/guides/build/projects/creating-a-new-project).

## Getting started

First, install your Dagster code location as a Python package. By using the --editable flag, pip will install your Python package in ["editable mode"](https://pip.pypa.io/en/latest/topics/local-project-installs/#editable-installs) so that as you develop, local code changes will automatically apply.
=======
<<<<<<< HEAD
This is the repo corresponding to the [Dagster crash course](https://dagster.io/blog/dagster-crash-course-oct-2022).

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/petehunt/dagster-github-stars-example)
=======
# my_dagster_project

This is a [Dagster](https://dagster.io/) project scaffolded with [`dagster project scaffold`](https://docs.dagster.io/getting-started/create-new-project).

## Getting started

First, install your Dagster repository as a Python package. By using the --editable flag, pip will install your repository in ["editable mode"](https://pip.pypa.io/en/latest/topics/local-project-installs/#editable-installs) so that as you develop, local code changes will automatically apply.
>>>>>>> 45a1796 (Initial commit')

```bash
pip install -e ".[dev]"
```

<<<<<<< HEAD
Then, start the Dagster UI web server:

```bash
dagster dev
=======
Then, start the Dagit web server:

```bash
dagit
>>>>>>> 45a1796 (Initial commit')
```

Open http://localhost:3000 with your browser to see the project.

<<<<<<< HEAD
You can start writing assets in `my_dagster_project/assets.py`. The assets are automatically loaded into the Dagster code location as you define them.

## Development

=======
You can start writing assets in `my_dagster_project/assets/`. The assets are automatically loaded into the Dagster repository as you define them.

## Development


>>>>>>> 45a1796 (Initial commit')
### Adding new Python dependencies

You can specify new Python dependencies in `setup.py`.

### Unit testing

Tests are in the `my_dagster_project_tests` directory and you can run tests using `pytest`:

```bash
pytest my_dagster_project_tests
```

### Schedules and sensors

<<<<<<< HEAD
If you want to enable Dagster [Schedules](https://docs.dagster.io/guides/automate/schedules/) or [Sensors](https://docs.dagster.io/guides/automate/sensors/) for your jobs, the [Dagster Daemon](https://docs.dagster.io/guides/deploy/execution/dagster-daemon) process must be running. This is done automatically when you run `dagster dev`.

Once your Dagster Daemon is running, you can start turning on schedules and sensors for your jobs.

## Deploy on Dagster+

The easiest way to deploy your Dagster project is to use Dagster+.

Check out the [Dagster+ documentation](https://docs.dagster.io/dagster-plus/) to learn more.
=======
If you want to enable Dagster [Schedules](https://docs.dagster.io/concepts/partitions-schedules-sensors/schedules) or [Sensors](https://docs.dagster.io/concepts/partitions-schedules-sensors/sensors) for your jobs, start the [Dagster Daemon](https://docs.dagster.io/deployment/dagster-daemon) process in the same folder as your `workspace.yaml` file, but in a different shell or terminal.

The `$DAGSTER_HOME` environment variable must be set to a directory for the daemon to work. Note: using directories within /tmp may cause issues. See [Dagster Instance default local behavior](https://docs.dagster.io/deployment/dagster-instance#default-local-behavior) for more details.

```bash
dagster-daemon run
```

Once your Dagster Daemon is running, you can start turning on schedules and sensors for your jobs.

## Deploy on Dagster Cloud

The easiest way to deploy your Dagster project is to use Dagster Cloud.

Check out the [Dagster Cloud Documentation](https://docs.dagster.cloud) to learn more.
>>>>>>> f9c3bb3 (Initial commit')
>>>>>>> 45a1796 (Initial commit')
