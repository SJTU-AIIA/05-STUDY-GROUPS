import json, os, glob, sys
from datetime import datetime, timezone, timedelta
from baselib import ROOT_DIR

def update_registry():
    """
    Keeps a studygroups.json file to keep track of all studygroups.
    """
    utc_8 = timezone(timedelta(hours=8))

    registry = {"studygroups": []}
    for groupinfo in glob.glob(os.path.join(str(ROOT_DIR),"[!.*]*/groupinfo.json")):
        try:
            with open(groupinfo) as f:
                data = json.load(f)
                # Add last_updated timestamp
                data["last_updated"] = datetime.now(utc_8).isoformat()
                if data["created"] == "":
                    data["created"] = data["last_updated"]
                registry["studygroups"].append(data)
        except:
            continue

    with open("studygroups.json", "w") as f:
        json.dump(registry, f, indent=2, sort_keys=True)

if __name__ == "__main__":
    update_registry()