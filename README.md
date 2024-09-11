# Readme

1. Create a JSON file with an object that has keys B, I, N, G, O (or any
letters). Each key's value is an array of bingo square options. See `test-squares.json` for example.
2. Create the cards!

```bash
python3 -m venv
source venv/bin/activate
python3 byob.py --json_file my-squares.json --output_dir mysquares 15
```

Then pull your tsv files into your favorite spreadsheet, format, print, and play!

`indexer.py` can make a useful index for folks if you have a lot of cards and
options.

