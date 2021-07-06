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

df = pd.DataFrame({"pre": [], "post": []})
ep.prepost(df)
```

## Group Comparison (ANOVA)
For group based comparison design (e.g. control group v.s. experiment group).

```
import pandas as pd

df = pd.DataFrame({"student_id": [1,2,3,4,5], "group": ["A", "B", "A", "B", "A"], "y": []})
ep.anova(df)
```

## Group Comparison (+Clustering)
It provides automatic K-means clustering, then compared the groups by ANOVA.


```
import pandas as pd

df = pd.DataFrame({"student_id": [1,2,3,4,5], "X": [[1,2],[1,3],[1,6],[3,3],[9.9]], "y": []})
ep.clustering(df, k=3) # k = cluster number
```