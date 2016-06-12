morning
=======

Abstracted modeling of objects, properties, and relationships. Morning provides
a series of classes for defining capturing systems for better serialization and
deserialization across multiple applications, without losing fidelity or
marginal information between transformations.

Model
-----

A Model is a collection of Properties or measurements and the internal
Relationships that ensure these properties are consistent. This means mulitple
redundant models can be used to capture a system within the same model--for
example, an orbit can be captured by classical orbital elements or by an
inertial state (position and velocity). Additional state information could be
extended by higher-fidelity applications. Otherwiae, different models would have
realized by multiple classes, with all the inter-object conversions required to
replicate the same behaviors.

A key requirement of redundant property modeling is the definition of accessors
that, when an value is assigned to a property, any related properties are
updated as part of the assignment using the model's Relationships. See Model
documentation for more details.

Properties
----------

A property is a value (measurement) identifying a particular state of a model.
Every property is is associated with a specific set of units (as provided by
Pint, one of the world's most awesome Python packages). A property also has an
associated uncertainty. Eventually, there are plans to define a specific frame
for property measurement, as well, but the implementation is still uncertain.

Relationships
-------------

A relationship defines how two or more model properties are related. (A
relationship can also include a single property, in which case it is exclusively
a constraint and may include an inequality). Relationships are defined in
symbolic Python expressions so they can be 'solved' for specific values.
