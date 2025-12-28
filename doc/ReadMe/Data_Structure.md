## Python Data Structures (Quick Differences)

| Python DS     | Java Equivalent              | Ordered? | Duplicates? | Mutable? | Index access? | Key uniqueness? | Typical use | Example (assign to variable) |
|--------------|------------------------------|----------|-------------|----------|---------------|-----------------|-------------|------------------------------|
| `list`       | `ArrayList`                  | ✅ Yes   | ✅ Allowed  | ✅ Yes   | ✅ Yes         | N/A             | Ordered collection, can contain duplicates | `x = [1, "A", 1]` |
| `tuple`      | Immutable list (concept)     | ✅ Yes   | ✅ Allowed  | ❌ No    | ✅ Yes         | N/A             | Fixed data, safe to share; can be key if items are hashable | `x = (1, "A", 1)` |
| `set`        | `HashSet`                    | ❌ No*   | ❌ No (Unique) | ✅ Yes | ❌ No          | N/A             | Remove duplicates, fast membership checks | `x = {1, "A"}` |
| `frozenset`  | Immutable `HashSet` (concept)| ❌ No*   | ❌ No (Unique) | ❌ No | ❌ No          | N/A             | Immutable set; can be dict key | `x = frozenset({1, "A"})` |
| `dict`       | `HashMap`                    | ✅ Yes** | Values: ✅ Allowed | ✅ Yes | By key ✅       | Keys: ✅ Unique  | Key-value storage, fast lookup by key | `x = {"id": 1, "name": "A"}` |

\* Sets are not sorted. They may look consistent sometimes, but you should not rely on order.
\** Dicts preserve insertion order in modern Python (3.7+ guaranteed).
