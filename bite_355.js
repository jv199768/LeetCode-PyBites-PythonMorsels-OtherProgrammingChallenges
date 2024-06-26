const typer = require('typer');
const time = require('time');
const { track } = require('rich/progress');
const algo = require('./algo');

const app = typer.Typer();
app.addTyper(algo.app, { name: "algo" });

app.command('sum', (a = typer.Argument({ help: "The value of the first summand", showDefault: false }), b = typer.Argument({ help: "The value of the second summand", showDefault: false })) => {
    typer.echo(`The sum of ${a} and ${b} is ${a + b}.`);
    let total = 0;
    for (const value of track(range(2), { description: "Processing..." })) {
        // Fake processing time
        time.sleep(0.01);
        total += 1;
    }
    console.log(`Processed ${total} things.`);
});

app.command('compare', (d, c) => {
    if (d > c) {
        typer.echo(`d=${d} is greater than c=${c}.`);
    } else if (c > d) {
        typer.echo(`d=${d} is lesser than c=${c}.`);
    }
    let total = 0;
    for (const value of track(range(2), { description: "Processing..." })) {
        // Fake processing time
        time.sleep(0.01);
        total += 1;
    }
    console.log(`Processed ${total} things.`);
});

if (require.main === module) {
    app();
}

