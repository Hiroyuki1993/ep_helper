# ep_helper

EP helper allows you to publish your data to Evidence Portal.

# Install

`pip install git+https://github.com/Hiroyuki1993/ep_helper`

# Usage

Initialize instance

```
from evidenceportal import API

ep = API(
    url="http://[host_to_evidence_portal]/evidence-portal-api"
)
```

## Pre/Post Design
For pre/post comparison of bunch of students.

```
import pandas as pd

df = pd.DataFrame({"student_id":[1,2,3,4,5], "pre": [1.2, 3.2, 4.1, 2.3, 1.4], "post": [2.2, 4.4, 2.3, 5.5, 3.9]})
ep.prepost(df)
```

## Group Comparison (ANOVA)
For group based comparison design (e.g. control group v.s. experiment group).

```
import pandas as pd

df = pd.DataFrame({"student_id": [1,2,3,4,5], "group": ["A", "B", "A", "B", "A"], "y": [2.2, 1.1, 3.3, 4.4, 5.5]})
ep.anova(df)
```
