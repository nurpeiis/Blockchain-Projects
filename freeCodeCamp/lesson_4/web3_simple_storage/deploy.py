import json
from solcx import compile_standard, install_solc


with open('./SimpleStorage.sol', 'r') as f:
    simple_storage_file = f.read()

# Compile solidity

compiled_sol = compile_standard(
    {
        'language': 'Solidity',
        'sources': {'SimpleStorage.sol': {'content': simple_storage_file}},
        'settings': {
            'outputSelection': {
                '*': {'*': ['abi', 'metadata', 'evm.bytecode', 'evm.sourceMap']}
            }
        }
    },
    solc_version='0.8.0',
)

# print(compiled_sol)

with open('compiled_code.json', 'w') as f:
    json.dump(compiled_sol, f)


# get bytecode
bytecode = compiled_sol['contracts']['SimpleStorage.sol']['SimpleStorage']['evm']['bytecode']['object']

# get abi
abi = compiled_sol['contracts']['SimpleStorage.sol']['SimpleStorage']['abi']

print(abi)
