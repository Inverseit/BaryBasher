
# Bary basher
The project is a verifier for elementary Euclidian Geometry facts.

Run the following command on your terminal within the directory of the project:

pip install -r requirements.txt

To have your problem verified, simply write the problem condition in the form that the interface below describes and see how your geomtry problem is bashed in several seconds.



## Example

Here we prove a famous symmedian lemma

![Theorem diagram](https://upload.wikimedia.org/wikipedia/commons/2/2f/Symmedian_Construction.png)

```python
ABC = Triangle(core.a, core.b, core.c)
A, B, C = ABC.getVertices()
D = ABC.getTangent("B").intersectWith(ABC.getTangent("C"))
K = ABC.getPoint("K") # Symmedian point
A_symmedian = Line(points=[A, K])

assert(A_symmedian.contains(D)) #resolves to true
```

  
