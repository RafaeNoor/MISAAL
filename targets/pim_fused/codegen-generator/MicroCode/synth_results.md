# Synthesized expressions

This file contains the synthesized micro-op programs for different configurations


## Bitvector Addition

### AP

Number of Bit Registers: 2

```
(list
(ReadSA 1)
(XNOR (Reg 1) (SA) (Reg 0))
(ReadSA 0)
(SEL (Reg 0) (Reg 1) (Reg 0) (SA))
(XNOR (SA) (SA) (Reg 1))
(WriteOut (SA))
)
```



### Flex

Number of Bit Registers: 2

```
(list
 (ReadSA 1)
 (XOR (Reg 1) (Reg 0) (SA))
 (ReadSA 0)
 (SEL (Reg 0) (Reg 1) (SA) (Reg 0))
 (XOR (SA) (SA) (Reg 1))
 (WriteOut (SA))
 )
```


## DRISA-NOR
```
(list
(OR (Reg 1) (Reg 0) (Reg 2))
(ReadSA 0)
(AND (Reg 2) (Reg 1) (SA))
(NOR (Reg 1) (Reg 1) (SA))
(NOR (Reg 0) (Reg 1) (Reg 2))
(ReadSA 1)
(NOR (Reg 1) (Reg 0) (SA))
(AND (Reg 0) (Reg 0) (SA))
(NOR (SA) (Reg 0) (Reg 1))
(WriteOut (SA))
)
```


## DRISA-MIXED
```
(list
 (NOR (Reg 1) (SA) (Reg 1))
 (XNOR (Reg 1) (Reg 1) (Reg 0))
 (ReadSA 1)
 (NAND (Reg 0) (Reg 1) (SA))
 (XNOR (Reg 1) (SA) (Reg 1))
 (ReadSA 0)
 (XNOR (SA) (Reg 1) (SA))
 (WriteOut (SA))
 )
```

## NAND-Only

```
(list
 (ReadSA 0)
 (NAND (Reg 0) (SA) (Reg 1))
 (NAND (SA) (Reg 0) (SA))
 (NAND (Reg 0) (Reg 0) (Reg 1))
 (NAND (Reg 0) (SA) (Reg 0))
 (ReadSA 1)
 (NAND (Reg 1) (SA) (Reg 0))
 (NAND (SA) (Reg 1) (SA))
 (NAND (Reg 0) (Reg 1) (Reg 0))
 (NAND (SA) (SA) (Reg 0))
 (WriteOut (SA))
 (NAND (Reg 1) (Reg 1) (Reg 1)))
```
