const typer = require('typer-cli');

const app = typer.Typer();

app.command('add', (a = typer.Argument({
  help: 'The value of the first summand',
  showDefault: false
}), b = typer.Argument({
  help: 'The value of the second summand',
  showDefault: false
})) => {
  typer.echo(`The sum of ${a} and ${b} is ${a + b}.`);
});

if (require.main === module) {
  app();
}

