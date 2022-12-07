use clap::{Arg, App};
use lib::{run, Config};

fn main() {
    // command-line interface
    let matches = App::new("minifind")
        .version("0.1.0")
        .author("calvin d. woo <calvin.d.woo@gmail.com>")
        .about("Find files that matches a regex pattern")
        .arg(
            Arg::with_name("patterns")
                .short('p')
                .help("List of file patterns to find.")
                .takes_value(true)
                .required(true)
                .multiple_values(true),
        )
        .arg(
            Arg::with_name("output")
                .short('o')
                .help("Write results to output file instead of stdout.")
                .takes_value(true)
                .required(false),
        )
        .arg(
            Arg::with_name("dirs")
                .short('d')
                .help("Directory to search matched filenames from.")
                .takes_value(true)
                .required(true)
                .multiple_values(true),
        )
        .arg(
            Arg::with_name("size")
                .short('s')
                .help("Minimum size (in bytes) a matched file needs to be reported.")
                .takes_value(true)
                .required(false),
        )
        .get_matches();

    let args = Config::from_args(&matches);

    if let Err(err) = run(&args) {
        panic!("{}", err)
    }
}
