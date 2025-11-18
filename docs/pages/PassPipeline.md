[\[<< Property Base Class\]](./Property.md)  [\[Overview\]](../Overview.md) [\[>> MISAAL Properties\]](./MISAAL_Properties.md)

# MISAAL Pass Pipeline Framework

The MISAAL Pass Pipeline framework provides a structured way to implement and execute compiler passes for semantic property analysis. The framework consists of two main classes: `MISAAL_PASS` (the base class for individual passes) and `MISAAL_PASS_PIPELINE` (the orchestrator for executing multiple passes in sequence).

## MISAAL_PASS Base Class

The `MISAAL_PASS` class serves as an abstract base class for implementing individual compiler passes in MISAAL. Each pass represents a specific analysis or transformation step in the semantic property compilation process.

### Key Components

1. **Pass Configuration**
   - `pass_name`: Unique identifier for the pass
   - `pass_description`: Detailed description of what the pass does
   - `parallelize`: Boolean flag to enable/disable parallel execution
   - `pool`: Number of parallel workers (default: 4)
   - `batch_size`: Size of batches for processing (default: 1024)
   - `working_directory`: Directory for pass-specific temporary files
   - `log_file`: Path to the log file for pass execution details
   - `pass_configs`: Dictionary of pass-specific configurations (see Pass-Specific Configurations section)

2. **Required Abstract Methods**
```python
@abstractclassmethod
def get_pass_name(cls):
    """Return the unique name of the pass"""

@abstractclassmethod
def get_pass_description(cls):
    """Return a detailed description of the pass"""

@abstractmethod
def get_results_summary(self):
    """Return a summary of the pass execution results"""

@abstractmethod
def get_pass_results(self):
    """Return the complete results of the pass execution"""

@abstractmethod
def execute(self):
    """Main execution method for the pass"""
```

3. **Dependency Management**
```python
@classmethod
def pass_depends_on(self):
    """Define dependencies on other passes"""
    return []

def set_dependency_results(self, pass_name, results):
    """Access results from dependent passes"""
```

4. **Logging Infrastructure**
   - Automatic logging of pass initialization
   - Execution progress tracking
   - Exception handling and logging
   - Execution time measurement
   - Results summary logging

## MISAAL_PASS_PIPELINE Class

The `MISAAL_PASS_PIPELINE` class orchestrates the execution of multiple passes in a specific order, handling dependencies and maintaining the overall execution state.

### Features

1. **Pipeline Configuration**
   - Configurable parallelization settings
   - Environment validation
   - Dependency validation
   - Centralized logging
   - DSL list management for source and target languages
   - Pass-specific configuration management

2. **Environment Validation**
   The pipeline validates required environment variables and Python paths:
   - Required variables: `MISAAL_SRC`, `HYDRIDE_ROOT`, `PYTHONPATH`
   - Required Python paths: `code-synthesizer`, `codegen-generator`

3. **Pipeline Execution Flow**
   1. Initialize logging infrastructure
   2. Validate environment and dependencies
   3. Execute passes in sequence
   4. Handle pass dependencies
   5. Maintain results from each pass
   6. Provide detailed execution logs

### Pass-Specific Configurations

The pipeline supports pass-specific configurations through the `pass_configs` parameter. This allows you to customize the behavior of individual passes without modifying their implementation:

```python
pass_configs = {
    "PassName": [
        ("config_param1", value1),
        ("config_param2", value2)
    ]
}

pipeline = MISAAL_PASS_PIPELINE(
    passes=passes,
    pass_configs=pass_configs,
    # ... other configurations ...
)
```

### Example Usage

```python
# Define passes
passes = [Pass1, Pass2, Pass3]

# Define pass-specific configurations
pass_configs = {
    "Pass1": [
        ("forward_map_path", "/path/to/forward_map.json"),
        ("depth", 3)
    ]
}

# Create pipeline
pipeline = MISAAL_PASS_PIPELINE(
    passes=passes,
    parallelize=True,
    pool=4,
    batch_size=1024,
    working_directory="/path/to/work/dir",
    log_file="/path/to/log.txt",
    pass_configs=pass_configs
)

# Execute pipeline
success = pipeline.execute_pass_pipeline()
```

## Available Passes

MISAAL includes several pre-implemented passes in the `lib/passes` directory:

1. **AutoLLVMEnumerate**
   - Purpose: Identifies equivalent expressions and enumerates patterns for AutoLLVM IR translation
   - Implementation: `AutoLLVMEnumerate.py`
   - Key Features:
     - Combines EqClassEqualDepthV4 and EnumeratePattern properties
     - Identifies equivalent expressions up to a specified depth
     - Generates all possible output patterns for AutoLLVM IR classes
     - Supports parallel execution for performance
   - Configuration Parameters:
     - `forward_map_path`: Path to the forward mapping JSON file
     - `output_depth`: Maximum depth for output expressions
     - `input_depth`: Maximum depth for input expressions
     - `depth_range`: Whether to explore all depths up to max
     - `use_canon_map`: Whether to use canonical form mapping
     - `bidirectional_test`: Whether to test both directions
   - Output:
     - Generates equivalence classes and enumerated patterns
     - Results are organized by property name in the output
     - Saves detailed JSON files for each analysis stage

2. **CommutativePass**
   - Purpose: Identifies commutative properties in DSL Instructions
   - Implementation: `CommutativePass.py`
   - Key Features:
     - Analyzes both source and target DSL instructions
     - Generates commutative equivalence classes
     - Produces a commutative map for use by other passes
     - Supports parallel execution for performance
   - Output:
     - Generates property results and commutative maps
     - Results are saved as JSON files in the working directory

3. **ComputeOnlyRelevancePass**
   - Purpose: Analyzes computational semantics similarities between DSL Instructions
   - Implementation: `ComputeOnlyRelevancePass.py`
   - Dependencies: Requires `CommutativePass` results
   - Key Features:
     - Multi-stage analysis using different repair relevance checks:
       - RepairRelevanceV4
       - RepairRelevanceIntermediates
       - Optional post-processing stage
     - Merges results from multiple repair instances
     - Handles data movement independence
   - Output:
     - Generates repair maps showing semantic relationships
     - Produces detailed JSON output for each analysis stage
     - Creates a combined results file for all analyses


## See Also
- [Property Base Class](./Property.md)
- [MISAAL Properties](./MISAAL_Properties.md)
- [TRS Compiler](./TRS_Compiler.md) 
