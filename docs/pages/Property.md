[\[<< AutoLLVM IR Representation\]](./AutoLLVM.md)   [\[>> Example of MISAAL Semantic Properties\]](./MISAAL_Properties.md)
# Property Base Class
At the core of <tt>MISAAL</tt> is the `Property` Base class which represents extracting a semantic property on the AutoLLVM IR (as well as Frontend IR). The code for the `Property` base class is described in [{MISAAL_ROOT}/lib/properties/Property.py](../../lib/properties/Property.py). Specific properties inherit from this class as part of their implementation. 


The components in evaluating semantic properties in <tt>MISAAL</tt> requires implementing the following functions.
### Member Functions
1. **Generating candidates**: Returns either a `List` or a Python `Generator` of 'candidates'. The candidates can be anything, but usually are either combinations of `DSLInstruction`, `Context`, or other semantics metadata.
```python
    def generate_candidates(self):
        raise NotImplementedError()
```

2. **Serializing Candidate**: Returns a Python `str` to be used as a key as part of the `dict` when saving the results of the property evaluation. Each candidate must uniquely map to a specific key.
```Python
    def serialize_candidate(self, candidate):
        raise NotImplementedError()
```


3. **Testing if property holds**: Returns a boolean whether the property being tested on the 'candidate' holds. If the property requires additionally other datastructures, it is up to the property developer to save such data in the `self` object.
```python
  def property_holds_on_candidate(self, candidate):
        raise NotImplementedError()
```

4. **Getting Property Result for candidate**: If the property being tested holds on a specific candidate, this should return the result of said property.
```Python
    def get_property_on_candidate(self, candidate):
        raise NotImplementedError()
```

5. **Optional Notification**: After a batch of candidates are evaluate, the summary of the results can be sent to the email of the user. The following functions can be overriden to describe the email structure.
```Python
    def notify(self, count, success_count ,start_time):
        msg_subject = self.get_notify_subject()
        msg_body = self.get_notify_body(count, success_count,  start_time)
        send_email(self.notify_to, msg_subject, msg_body)

    def get_notify_subject(self):
        pass


    def get_notify_body(self, count, success_count, start_time):
        pass
```

## High Level Flow

Once the above functions are implemented the flow for evaluating properties is quite obvious. Candidates are generated and evaluated. As candidates are independent of each other, they can be evaluated in parallel. The parallelism can be controlled by specifying the `parallel` boolean in the constructor for a property. `BATCH_SIZE` controls the number of candidates in one batch of evaluation, after which notification to the user is done via email (if enabled). `POOL_SIZE` controls the number of parallel workers executing simultaneously. 

