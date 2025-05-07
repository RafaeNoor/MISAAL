[\[<< Semantic Property Base Class\]](./Property.md)   [\[>> Concretization Grammar\]](./Grammar.md)
# Important Properties used in MISAAL
<tt>MISAAL</tt> provides various important semantic properties from which retargetable rewrite rules can be derived. This page lists and briefly describes these properties. 


## Commutative
The commutative property identidies which symbolic parameters for AutoLLVM IR operations can commute which each other. For Binary Operators a simple boolean is sufficient, but for operations with multiple operands, the list of operand indices which can commute are identified. This is used to produce the `commutative_map.json` file which is used to prune commutative variants of AutoLLVM IR / Frontend IR operations greatly reducing the number of expressions which need to be enumerated. 

## Associative & Distributive
Example of properties which identify when expressions are Associative or Distributive. These properties, as well as all other properties, invoke `Rosette` to symbolically verify that the expressions are equivalent, and hence the property holds. 

## Identify Swizzles
Analyzes and executes the semantics of each `Context` (i.e. target instruction) to extract data access patterns. These data access patterns are used to create swizzle patterns which are initially represented using shuffle vector masks (similar to representation in `LLVM`). Post processing scripts then convert these masks into pseudo-code, which are then converted into formal semantics and AutoLLVM. More details of the post-processing and swizzle generation flow are provided in the [Swizzle Documentation](./Swizzles.md]).

## LowerSwizzles
Enumerates AutoLLVM IR expressions such that the left-hand side expressions are in terms of AutoLLVM IR swizzle operations and right-hand side expressions are in terms of AutoLLVM IR non-swizzle operations (i.e. operations which directly correspond to target specific instructions). These are used to generate the swizzle lowering rules.


## RepairRelevanceV4 & RepairRelevanceIntermediates
RepairRelevanceV4 implements the Compute-Only instruction relevance described in the <tt>MISAAL</tt> publication, where as `RepairRelevanceIntermediates` implements the generalized version of the Compute-Only instruction relevance. The `RDSL` for this is described the [RDSL Semantic Dictionary](../../lib/sema/repairs_sema.py). These properties produce possibly overlapping relevance sets which are often described in files named `repair_map_{frontend}_{target}.json`.

## RepairRelavancePostProcess
Repair Relevance may identify certain AutoLLVM IR operations to be relevant, which while true are not exactly useful since they may be achieved using some identity. For example multiplication by 0 or 1, minimum / maximum of the same value, or addition by 0. These cases can be post-processed and cleaned out using these properties to further refine the Relevance sets.


## EqClassEqualDepthV4
Performs the enumeration of AutoLLVM IR, Swizzles and Frontend IR expressions to identify pairs of expression `templates` which represent possible valid rewrite rules. This property consumes the `repair_map_*.json` files to enumerate expressions appropriately. Other variants of these properties, with the prefix `EqClassEqualDepth` allow different forms of enumeration for those interested. 


## EnumeratePattern
Takes the rewrite rule templates derived from the `EqClassEqualDepth*` properties and extracts possible valid "_Concretizations_" of the rewrite rule template (Please refer to the <tt>MISAAL</tt> publication for understanding what Concretization and Abstraction refers to). Once these concrete rewrite rules are extracted from the templates, they can be further abstracted into a high order rewrite rule. Details of rewrite rule abstraction are described in the [Rewrite Rule Documentation](./Patterns.md).