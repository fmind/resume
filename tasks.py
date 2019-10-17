from invoke import task


@task
def view(c):
    """View the resume."""
    c.run("xdg-open resume.pdf")


@task
def work(c):
    """Build the resume on change."""
    c.run("watchmedo tricks tricks.yaml")
