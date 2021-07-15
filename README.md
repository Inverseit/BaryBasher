
# Bary basher

Just write the problem condition in the form that interface describes and see how your geomtry problem is bashed in several seconds.



## Example

Here we prove a famous symmedian lemma


```python
ABC = Triangle(core.a, core.b, core.c)
A, B, C = ABC.getVertices()
w = ABC.get_circumcircle()
tangentB = ABC.getTangent("B")
tangentC = ABC.getTangent("C")

L = tangentB.intersectWith(tangentC)
K = ABC.getPoint("K") # Symmedian point
A_symmedian = Line(points=[A, K])

assert(A_symmedian.contains(L)) #resolves to true
```

  
