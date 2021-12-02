
# Bary basher
The project is a verifier for elementary Euclidian Geometry facts.

Run the following command on your terminal within the directory of the project:

pip install -r requirements.txt

To have your problem verified, simply write the problem condition in the form that the interface below describes and see how your geomtry problem is bashed in several seconds.



## Example

Here we prove a famous symmedian lemma


```python
ABC = Triangle(core.a, core.b, core.c)
A, B, C = ABC.getVertices()
tangentB = ABC.getTangent("B")
tangentC = ABC.getTangent("C")

L = tangentB.intersectWith(tangentC)
K = ABC.getPoint("K") # Symmedian point
A_symmedian = Line(points=[A, K])

assert(A_symmedian.contains(L)) #resolves to true
```

  
