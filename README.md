# Islands of Insight Helper
A tool to make your gameplay experience more enjoyable!

Modify an Islands of Insight .sav file as described below. The tool 
prints out some gameplay statistics even if no modifications are requested. 

## How To

```bash
pip install ioihelper

# installs jsonpath_ng, pygvas and pydantic as requirements
# Close the game, use this utility as described below, then restart.
```

```commandline
> ioihelper -h
usage: ioihelper [-h] 
        [--sb, --set_sparks_balance SET_SPARKS_BALANCE]
        [--sv, --show_completed_visuals SHOW_COMPLETED_VISUALS] 
        [--complete_all_dailies]
        [--bk, --backup_old_and_use_new] 
        [--if, --input_file INPUT_FILE] 
        [--hf, --hints_file HINTS_FILE] 
        [--sj, --save_json] 

Modify an Islands of Insight .sav file (OfflineSavegame.sav) as requested. Will 
prints out some gameplay statistics if no modifications are requested.

options:
  -h, --help            
        Show this help message and exit
  --set_sparks_balance, --sb SET_SPARKS_BALANCE
        Sets the Sparks (currency) in your account for purchasing cosmetics. 
        The ones you don't get through mainline and zone progression.
  --show_completed_visuals, --sv SHOW_COMPLETED_VISUALS
        Permanently enable/disable visuals cues for puzzle completion.
        Persists beyond the current play session.
  --complete_all_dailies
        Mark ALL dailies completed. This will grant all the progression 
        cosmetics, but the game will be less fun to play. It does NOT affect
        the meta puzzles or enclaves.
  --backup_old_and_use_new, --bk
        Without this flag your edits will not go into effect. This backs up the 
        original file by giving it a timestamp and renames the modified file so 
        it will be loaded by Islands of Insight.
  --input_file, --if INPUT_FILE
        Path to the Islands of Insight save file. If not present, looks for 
        your save file installation.
  --hints_file, --hf HINTS_FILE
        Path to optional deserialization hints (JSON) file. AFAIK, Islands 
        doesn't need one. See the pygvas documentation for more information.
  --save_json, --sj
        Save JSON save game files for both before and after modifications. 
        These will land next to the indicated save game source file.
```

## Dependencies
* Depends on 
  * The [jsonpath_ng JSONPath query library](https://pypi.org/project/jsonpath-ng/)
  * The [pygvas GVAS parsing library](https://github.com/Ryzhara/pygvas/blob/main/docs/gvas_overview.md) 
  * The [pydantic validation library (via pygvas)](https://docs.pydantic.dev/latest/).

## Caveats
* If your game save file is not in the standard location then you'll have to find
it and add its path to the command line.
* This utility tries very hard to not bork your file, but back it up anyhow.
    Because things happen(tm).

## Background
When the awsome puzzle game [Islands of Insight](https://store.steampowered.com/app/2071500/Islands_of_Insight/) 
went offline, the team converted the game for offline play. That conversion
required storing game progress locally. The team likely also wanted to improve
re-playability, so they changed some things to focus on that experience.

One change I didn't prefer was that completed puzzles were no longer persistently
visually marked for completion. Restarting the game would reset those visual markers, 
making it difficult to remember which puzzles would count toward zone-by-zone or 
puzzle-type progress. You can still earn Sparks, but progression didn't increment
when re-completing the same puzzle.

I decided to take matters into my own hands and figured out how to do the edits 
described in the command line directions.