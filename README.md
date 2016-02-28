CadQuery 2.0
========================================

This branch is a work in progress. It is the next major version of CQ, which will be a significant re-write
of the current release.

CadQuery Goals
-----------------

These goals are unchanged from CQ 0.X

CadQuery is an intuitive, easy-to-use python based language for building parametric 3D CAD models.  CadQuery is for 3D CAD what jQuery is for javascript.  Imagine selecting Faces of a 3d object the same way you select DOM objects with JQuery!

CadQuery has several goals:

* Build models with scripts that are as close as possible to how you'd describe the object to a human.
* Create parametric models that can be very easily customized by end users
* Output high quality CAD formats like STEP and AMF in addition to traditional STL
* Provide a non-proprietary, plain text model format that can be edited and executed with only a web browser

CQ 2.0 Changes
--------------------

* Based on pythonOCC/OCE, not on FreeCAD. FreeCAD got CQ started, but is too limiting going forward.
* Strict separation of CQ and its implementation. We want to support other CAD kernels later.
* Separate selector tree and feature tree.  In CQ 0.X, the feature tree and the selector tree were the same. This was a design decision that caused a lot of problems.  The two concepts need to be separate
* operationIds. Each operation can have an id, which can be used to select the features/solids created or modified by that operation
* created-by selectors. CQ 2.0 needs to support, from the ground-up, the ability to select features based on the operation that created them.
* provide more options about locating the origin on new workplanes
* easier to use plugin framework. plugins need to be separated more clearly from core code ( cbore, csk, for example )
* more separation between 3d primitives, 2d operations, selection operations, and modification operations
* the CQ object will server as a facade for other objects. It should not implement anything itself.
* much more modular code. we need code a lot easier to test and edit. 



How CQ 2.0 will work ( roughly)
--------------------------------

The Context
------------
Modeling will start with a Context. creating a new context will create a completely new starting point. 
Any global state will be stored in the context.

The feature tree
-----------------
Each context has a single feature tree. The feature tree stores the results of all of the operations.
Each time a solid is created or modified, a new node is created in the tree, which points to the node before it.
In MOST cases, the 'feature tree' will really be a line.  For example, consider the below CQ 0.3 code::

   a = CQ.Workplane('XY')
   b = b.box(1,2,3)
   c = b.faces(">Z").workplane().circle(2.0).extrude(1.0)
   d = b.faces(">Z").workplane().hole(0.1,thru=True)
   
Here, 'a' refers to the root node in the tree. This has no solid stored with the node 
'b' refers to a direct child of a.  A box is stored in this node
'c' refers to a direct child of b.  This node contains a box with a cylinder sticking out of the top
'd' also refers to a direct child of b. This node contains a box with a small hole in it.

Note the difference in behavior with CQ 0.3, when the same underlying solid would be shared with all of these references.
CQ 0.X attempts to save memory by removing old solids that are no longer referenced.  This version does not make that attempt--
as long as the user is holding a reference to a node in the tree, the solids will stay referenced.

Workplanes
-------------
Workplanes will remain mostly unchanged in CQ 2.0.  they represent a 2-d context, which can be used to locate geometry
relative to the selected plane. Just like in CQ 0.X, a user can create a workplane from one of the builtins, or from a selected
face. This implies accumulating 2-d geometry while the user is 'drawing' on it.

Unlike CQ 2.0, workplanes should ONLY provide 2d operations.  Code that does 3d operations should be located elsewhere.

geom.py
-----------
All standard geometry ( planes, vectors, points, transformations ) must be declared here.

Operations
-------------
Operations create or edit 3d features. Unlike CQ 0.X, operations will have an identifier, which allows selecting the features
of a solid that were created by that operation.  Users should be able to provide their own operations, which should make it
much more straightforward to extend cadquery.

Each operation must track the features ( wires, faces, edges, solids ) that were created or modified in that operation. For
example, a hole operation must list the cylindrical and circular face it created, and the upper face it modified. In some
cases, this is a trivial task, because the underlying OCE kernel provides this information. in other cases, it is more difficult
to obtain. 

the affected entities will be grouped by created, modified, and deleted, so that the category can be further used for selection.
Example::

    Workplane('XY').box(1,2,3).faces(">Z").hole(0.1,0.1, opId="hole01").faces(createdBy="hole01")
	
will select the new face at the bottom of the hole ( since it is the only face created by the hole), and::

	Workplane('XY').box(1,2,3).faces(">Z").hole(0.1,0.1, opId="hole01").faces(modifiedBy="hole01")::

will select the face on the top of the block, since it was modfied


Selectors
-----------
Just like CQ 0.X, selectors allow the user to find features, and then use them to build more geometry.
Unlike CQ 0.X, chained selectors are NOT the same as the feature tree itself, and can be created independently of the tree.

This should make the CQ code much more maintainable and readable.

When a Selector is created, it is given a single node in the feature tree. The solid geometry store in that node is the basis
for selection operations.  

in CQ 2.0, we should consider adding generalized select method, that will allow the user to combine entities of multiple types.
To support this, a constant will be added to narrow to entity types. For example::

     Workplane('XY').box(1,2,3).faces(">Z")
	 
is equivalent to::

	Workplane('XY').box(1,2,3).select( ">Z" && EntityType.FACES )
  
We need to figure out how to retain the simplicity of faces(">Z") while allowing boolean operations that allow keyword based
filters at the same time:  faces(">Z" && modifiedBy="hole01" ) 

  
Binding to Implementations
---------------------------
CQ 2.0 must be designed to support multiple backend implementations. As a result, operations, geometry, and selectors
must not directly include pythonOCC/OCE code. 

There are several ways that the code can support alternate backends.  I'm not sure the same approach will work best everywhere.
One way is to provide common base classes, and then require a separate backend implementation that overrides/implements various
functions. This would probably work well for Operations.

Another way would be to allow each backend to provide its own implementation of the entire package, and then link the correct
one in using the import system. for example, suppose we have geom_oce.py and geom_freecad.py-- but then we simply link
the proper one based on which seems to be available when we run.




The CQ.py facade class
-----------------------

CQ.py will act as a facade that glues the various components together. When the user performs an operation, the following
occurs:
* The operation is executed
* A new node in the feature tree is created, representing the result of the operation
* A new CQ selector is automatically created that points to the current node in the feature tree

This will mean that the CQ 2.0 syntax will be very similar to CQ 1.X syntax, but the underlying implementation will be very different

