import common.Types
import concurrent.futures

class Property:
    """Abstract class to represent properties for Hydride IR's Equivalence Classes

    """

    def __init__(self, name = "Property", dsl_list = [], synth_desc = None):
        """Class constructor for base class

        Args:
            name (str, optional): _description_. Defaults to "Property".
            dsl_list (list, optional): _description_. Defaults to [].
        """
        self.name = name
        self.dsl_list = dsl_list
        self.synth_desc = synth_desc

        # Candidates refer to expressions (usually tree's) on which the property will be 
        # analyzed.
        self.candidates = []

    def set_candidates(self, candidates):
        self.candidates = candidates

    def generate_candidates(self):
        raise NotImplementedError()


    def get_property_desc(self):
        """Abstract method for returning string which describes the property

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError()

    def property_holds_on_candidate(self, candidate):
        """Method for checking if property holds on candidate. This may on the returned
        value for the expression, or with respect to the semantics of the instruction.

        Args:
            instruction (DSLInstruction): Instruction (Equivalence class) on which the property is being inferred 

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError()

    def get_property_on_candidate(self, candidate):
        """Returns a python object which captures the relationship of the property on the candidate

        Args:
            candidate (DSLInstruction or Anything): Candidates could be single DSL instructions, DSL Expression Trees, or anything really.

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError()


    def serialize_candidate(self, candidate):
        """Serialize the candidate so that it can be used as a key in a python dictionary

        Args:
            candidate (_type_): _description_

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError()


    def get_hydride_import_header(self):
        return """
        #lang rosette
        (require rosette/lib/synthax)
        (require rosette/lib/angelic)
        (require racket/pretty)
        (require data/bit-vector)
        (require rosette/lib/destruct)
        (require rosette/solver/smt/boolector)
        (require hydride)
        
        ;; Uncomment the line below to enable verbose logging
        (enable-debug)
        (custodian-limit-memory (current-custodian) (* 1000 1024 1024))
        """

    def get_property(self):
        """Main driver method for generating information for properties. In general, the flow would
        consist of generating candidates, checking if the property holds for each candidate and appropriately,
        and finally generating a python dictionary which maps candidates to properties
        """
        print(self.get_property_desc())

        self.set_candidates(
            self.generate_candidates()
        )


        property_map = {}

        print("Total Number of Candidates: ", len(self.candidates))
        candidate_count = 0
        # create a thread pool with 4 threads
        pool = concurrent.futures.ThreadPoolExecutor(max_workers=4)
        
        def worker(candidate):
            """Parallelizable method on each candidate

            Args:
                candidate (_type_): _description_
            """
            if self.property_holds_on_candidate(candidate):
                
                candidate_count += 1

                key = self.serialize_candidate(candidate)
                print(key)

                if key not in property_map:
                    property_map[key] = []
                property_map[key].append ({
                    "property_name": self.name,
                    "property": self.get_property_on_candidate(candidate) 
                })



        for candidate in self.candidates:
            pool.submit(worker, candidate)


        pool.shutdown(wait=True)

        print("Property", self.name, "holds on", candidate_count, "/", len(self.candidates), "candidates ...")

        return property_map







    