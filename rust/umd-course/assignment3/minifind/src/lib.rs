use clap::ArgMatches;
use regex::Regex;
use std::fs::File;


pub struct Config<'a> {
    pub dirs: Vec<&'a str>,
    pub patterns: Vec<&'a str>,
    pub output: Option<&'a str>,
    pub size: Option<&'a str>,
}

impl<'a> Config<'a> {
    pub fn from_args(args: &'a ArgMatches) -> Self {
        Config {
            dirs: args.values_of("dirs").unwrap().collect(),
            patterns: args.values_of("patterns").unwrap().collect(),
            output: args.value_of("output"),
            size: args.value_of("size")
        }
    }
}

pub fn run(config: &Config) -> Result<(), &'static str> {
    // parse patterns
    let v_pats: Vec<Regex> = config.parse_patterns()?;

    Ok(())
}
