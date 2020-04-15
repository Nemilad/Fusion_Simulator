Macro_command_list = ('ADD', 'SUB', 'INC', 'DEC', 'ADC', 'SBB', 'CMP', 'TEST', 'AND', 'OR', 'XOR', 'NOT', 'NEG',
                      'JMP', 'MOV', 'MUL', 'DIV', 'JA', 'JNA', 'JAE', 'JNAE', 'JB', 'JNB', 'JBE', 'JNBE', 'JC', 'JNC',
                      'JE', 'JNE', 'JG', 'JNG', 'JGE', 'JNGE', 'JL', 'JNL', 'JLE', 'JNLE', 'JS', 'JNS', 'JO', 'JNO',
                      'JP', 'JNP', 'JPO', 'JPE', 'JZ', 'JNZ', 'JCXZ', 'JECXZ', 'JRCXZ', 'LOOP')

Macro_micro_dict = {
    'ADD': {
        'Reg_Reg': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg_Imm': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg_Mem': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem_Reg': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 1,
            'WRITE': 1
        },
        'Mem_Imm': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 1,
            'WRITE': 1
        },
    },
    'SUB': {
        'Reg_Reg': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg_Imm': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg_Mem': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem_Reg': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 1,
            'WRITE': 1
        },
        'Mem_Imm': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 1,
            'WRITE': 1
        },
    },
    'INC': {
        'Reg': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 1,
            'WRITE': 1
        },
    },
    'DEC': {
        'Reg': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 1,
            'WRITE': 1
        },
    },
    'ADC': {
        'Reg_Reg': {
            'READ': 0,
            'MODIFY': 2,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg_Imm': {
            'READ': 0,
            'MODIFY': 2,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg_Mem': {
            'READ': 1,
            'MODIFY': 2,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem_Reg': {
            'READ': 1,
            'MODIFY': 4,
            'ADDRESS': 1,
            'WRITE': 1
        },
        'Mem_Imm': {
            'READ': 1,
            'MODIFY': 4,
            'ADDRESS': 1,
            'WRITE': 1
        },
    },
    'SBB': {
        'Reg_Reg': {
            'READ': 0,
            'MODIFY': 2,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg_Imm': {
            'READ': 0,
            'MODIFY': 2,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg_Mem': {
            'READ': 1,
            'MODIFY': 2,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem_Reg': {
            'READ': 1,
            'MODIFY': 4,
            'ADDRESS': 1,
            'WRITE': 1
        },
        'Mem_Imm': {
            'READ': 1,
            'MODIFY': 4,
            'ADDRESS': 1,
            'WRITE': 1
        },
    },
    'CMP': {
        'Reg_Reg': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg_Imm': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem_Reg': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem_Imm': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
    },
    'TEST': {
        'Reg_Reg': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg_Imm': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg_Mem': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem_Imm': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
    },
    'AND': {
        'Reg_Reg': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg_Imm': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg_Mem': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem_Reg': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 1,
            'WRITE': 1
        },
        'Mem_Imm': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 1,
            'WRITE': 1
        },
    },
    'OR': {
        'Reg_Reg': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg_Imm': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg_Mem': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem_Reg': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 1,
            'WRITE': 1
        },
        'Mem_Imm': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 1,
            'WRITE': 1
        },
    },
    'XOR': {
        'Reg_Reg': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg_Imm': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg_Mem': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem_Reg': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 1,
            'WRITE': 1
        },
        'Mem_Imm': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 1,
            'WRITE': 1
        },
    },
    'NOT': {
        'Reg': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 1,
            'WRITE': 1
        },
    },
    'NEG': {
        'Reg': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 1,
            'WRITE': 1
        },
    },
    'JMP': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        }
    },
    'MOV': {
        'Reg_Reg': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg_Imm': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg_Mem': {
            'READ': 1,
            'MODIFY': 0,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem_Reg': {
            'READ': 0,
            'MODIFY': 0,
            'ADDRESS': 1,
            'WRITE': 1
        },
        'Mem_Imm': {
            'READ': 0,
            'MODIFY': 0,
            'ADDRESS': 1,
            'WRITE': 1
        },
    },
    'MUL': {
        'Reg8': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg16': {
            'READ': 0,
            'MODIFY': 3,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg32': {
            'READ': 0,
            'MODIFY': 3,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem8': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem16': {
            'READ': 1,
            'MODIFY': 3,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem32': {
            'READ': 1,
            'MODIFY': 3,
            'ADDRESS': 0,
            'WRITE': 0
        },
    },
    'DIV': {
        'Reg8': {
            'READ': 0,
            'MODIFY': 5,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg16': {
            'READ': 0,
            'MODIFY': 4,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg32': {
            'READ': 0,
            'MODIFY': 4,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem8': {
            'READ': 1,
            'MODIFY': 5,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem16': {
            'READ': 1,
            'MODIFY': 4,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem32': {
            'READ': 1,
            'MODIFY': 4,
            'ADDRESS': 0,
            'WRITE': 0
        },
    },
    'JA': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        }
    },
    'JNA': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        }
    },
    'JAE': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        }
    },
    'JNAE': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        }
    },
    'JB': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        }
    },
    'JNB': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        }
    },
    'JBE': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        }
    },
    'JNBE': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        }
    },
    'JC': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        }
    },
    'JNC': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        }
    },
    'JE': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        }
    },
    'JNE': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        }
    },
    'JG': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        }
    },
    'JNG': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        }
    },
    'JGE': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        }
    },
    'JNGE': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        }
    },
    'JL': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        }
    },
    'JNL': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        }
    },
    'JLE': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        }
    },
    'JNLE': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        }
    },
    'JS': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        }
    },
    'JNS': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        }
    },
    'JO': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        }
    },
    'JNO': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        }
    },
    'JP': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        }
    },
    'JNP': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        }
    },
    'JPO': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        }
    },
    'JPE': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        }
    },
    'JZ': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        }
    },
    'JNZ': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        }
    },
    'JCXZ': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 2,
            'ADDRESS': 0,
            'WRITE': 0
        }
    },
    'JECXZ': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 2,
            'ADDRESS': 0,
            'WRITE': 0
        }
    },
    'LOOP': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 11,
            'ADDRESS': 0,
            'WRITE': 0
        }
    }
}

Macro_micro_dict_Core_2 = {
    'ADD': {

    },
    'SUB': {

    },
    'INC': {

    },
    'DEC': {

    },
    'ADC': {

    },
    'SBB': {

    },
    'CMP': {

    },
    'TEST': {

    },

    'AND': {

    },
    'OR': {

    },
    'XOR': {

    },
    'NOT': {

    },
    'NEG': {

    },
    'JMP': {

    },
    'MOV': {

    },
    'MUL': {
        'Reg64': {
            'READ': 0,
            'MODIFY': 3,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem64': {
            'READ': 1,
            'MODIFY': 2,
            'ADDRESS': 0,
            'WRITE': 0
        },
    },
    'DIV': {
        'Reg8': {
            'READ': 0,
            'MODIFY': 4,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg16': {
            'READ': 0,
            'MODIFY': 7,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg32': {
            'READ': 0,
            'MODIFY': 7,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg64': {
            'READ': 0,
            'MODIFY': 32,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem8': {
            'READ': 1,
            'MODIFY': 3,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem16': {
            'READ': 1,
            'MODIFY': 7,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem32': {
            'READ': 1,
            'MODIFY': 6,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem64': {
            'READ': 1,
            'MODIFY': 31,
            'ADDRESS': 0,
            'WRITE': 0
        },
    },
    'JA': {

    },
    'JNA': {

    },
    'JAE': {

    },
    'JNAE': {

    },
    'JB': {

    },
    'JNB': {

    },
    'JBE': {

    },
    'JNBE': {

    },
    'JC': {

    },
    'JNC': {

    },
    'JE': {

    },
    'JNE': {

    },
    'JG': {

    },
    'JNG': {

    },
    'JGE': {

    },
    'JNGE': {

    },
    'JL': {

    },
    'JNL': {

    },
    'JLE': {

    },
    'JNLE': {

    },
    'JS': {

    },
    'JNS': {

    },
    'JO': {

    },
    'JNO': {

    },
    'JP': {

    },
    'JNP': {

    },
    'JPO': {

    },
    'JPE': {

    },
    'JZ': {

    },
    'JNZ': {

    },
    'JCXZ': {

    },
    'JECXZ': {

    },
    'JRCXZ': {

    },
    'LOOP': {

    }
}

Macro_micro_dict_Nehalem = {
    'ADD': {

    },
    'SUB': {

    },
    'INC': {

    },
    'DEC': {

    },
    'ADC': {
        'Mem_Reg': {
            'READ': 1,
            'MODIFY': 3,
            'ADDRESS': 1,
            'WRITE': 1
        },
        'Mem_Imm': {
            'READ': 1,
            'MODIFY': 3,
            'ADDRESS': 1,
            'WRITE': 1
        },
    },
    'SBB': {
        'Mem_Reg': {
            'READ': 1,
            'MODIFY': 3,
            'ADDRESS': 1,
            'WRITE': 1
        },
        'Mem_Imm': {
            'READ': 1,
            'MODIFY': 3,
            'ADDRESS': 1,
            'WRITE': 1
        },
    },
    'CMP': {

    },
    'TEST': {

    },
    'AND': {

    },
    'OR': {

    },
    'XOR': {

    },
    'NOT': {

    },
    'NEG': {

    },
    'JMP': {

    },
    'MOV': {
        'Reg_Reg': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg_Imm': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg_Mem': {
            'READ': 1,
            'MODIFY': 0,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem_Reg': {
            'READ': 0,
            'MODIFY': 0,
            'ADDRESS': 1,
            'WRITE': 1
        },
        'Mem_Imm': {
            'READ': 0,
            'MODIFY': 0,
            'ADDRESS': 1,
            'WRITE': 1
        },
    },
    'MUL': {
        'Reg8': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg16': {
            'READ': 0,
            'MODIFY': 3,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg32': {
            'READ': 0,
            'MODIFY': 3,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem8': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem16': {
            'READ': 1,
            'MODIFY': 3,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem32': {
            'READ': 1,
            'MODIFY': 3,
            'ADDRESS': 0,
            'WRITE': 0
        },
    },
    'DIV': {
        'Reg8': {
            'READ': 0,
            'MODIFY': 5,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg16': {
            'READ': 0,
            'MODIFY': 4,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg32': {
            'READ': 0,
            'MODIFY': 4,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem8': {
            'READ': 0,
            'MODIFY': 5,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem16': {
            'READ': 1,
            'MODIFY': 4,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem32': {
            'READ': 1,
            'MODIFY': 4,
            'ADDRESS': 0,
            'WRITE': 0
        },
    },
    'JA': {

    },
    'JNA': {

    },
    'JAE': {

    },
    'JNAE': {

    },
    'JB': {

    },
    'JNB': {

    },
    'JBE': {

    },
    'JNBE': {

    },
    'JC': {

    },
    'JNC': {

    },
    'JE': {

    },
    'JNE': {

    },
    'JG': {

    },
    'JNG': {

    },
    'JGE': {

    },
    'JNGE': {

    },
    'JL': {

    },
    'JNL': {

    },
    'JLE': {

    },
    'JNLE': {

    },
    'JS': {

    },
    'JNS': {

    },
    'JO': {

    },
    'JNO': {

    },
    'JP': {

    },
    'JNP': {

    },
    'JPO': {

    },
    'JPE': {

    },
    'JZ': {

    },
    'JNZ': {

    },
    'JCXZ': {

    },
    'JECXZ': {

    },
    'JRCXZ': {

    },
    'LOOP': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 6,
            'ADDRESS': 0,
            'WRITE': 0
        }
    }
}

Macro_micro_dict_Sandy_Bridge = {
    'ADD': {

    },
    'SUB': {

    },
    'INC': {

    },
    'DEC': {

    },
    'ADC': {
        'Mem_Reg': {
            'READ': 1,
            'MODIFY': 3,
            'ADDRESS': 1,
            'WRITE': 1
        },
        'Mem_Imm': {
            'READ': 1,
            'MODIFY': 3,
            'ADDRESS': 1,
            'WRITE': 1
        },
    },
    'SBB': {
        'Mem_Reg': {
            'READ': 1,
            'MODIFY': 3,
            'ADDRESS': 1,
            'WRITE': 1
        },
        'Mem_Imm': {
            'READ': 1,
            'MODIFY': 3,
            'ADDRESS': 1,
            'WRITE': 1
        },
    },
    'CMP': {

    },
    'TEST': {

    },
    'AND': {

    },
    'OR': {

    },
    'XOR': {

    },
    'NOT': {

    },
    'NEG': {

    },
    'JMP': {

    },
    'MOV': {

    },
    'MUL': {

        'Reg16': {
            'READ': 0,
            'MODIFY': 4,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg32': {
            'READ': 0,
            'MODIFY': 3,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg64': {
            'READ': 0,
            'MODIFY': 2,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem8': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem32': {
            'READ': 1,
            'MODIFY': 2,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem64': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
    },
    'DIV': {
        'Reg8': {
            'READ': 0,
            'MODIFY': 10,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg16': {
            'READ': 0,
            'MODIFY': 11,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg32': {
            'READ': 0,
            'MODIFY': 10,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg64': {
            'READ': 0,
            'MODIFY': 34,
            'ADDRESS': 0,
            'WRITE': 0
        },
    },
    'JA': {

    },
    'JNA': {

    },
    'JAE': {

    },
    'JNAE': {

    },
    'JB': {

    },
    'JNB': {

    },
    'JBE': {

    },
    'JNBE': {

    },
    'JC': {

    },
    'JNC': {

    },
    'JE': {

    },
    'JNE': {

    },
    'JG': {

    },
    'JNG': {

    },
    'JGE': {

    },
    'JNGE': {

    },
    'JL': {

    },
    'JNL': {

    },
    'JLE': {

    },
    'JNLE': {

    },
    'JS': {

    },
    'JNS': {

    },
    'JO': {

    },
    'JNO': {

    },
    'JP': {

    },
    'JNP': {

    },
    'JPO': {

    },
    'JPE': {

    },
    'JZ': {

    },
    'JNZ': {

    },
    'JCXZ': {

    },
    'JECXZ': {

    },
    'JRCXZ': {

    },
    'LOOP': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 7,
            'ADDRESS': 0,
            'WRITE': 0
        }
    }
}

Macro_micro_dict_Ivy_Bridge = {
    'ADD': {

    },
    'SUB': {

    },
    'INC': {

    },
    'DEC': {

    },
    'ADC': {
        'Mem_Reg': {
            'READ': 1,
            'MODIFY': 3,
            'ADDRESS': 1,
            'WRITE': 1
        },
        'Mem_Imm': {
            'READ': 1,
            'MODIFY': 3,
            'ADDRESS': 1,
            'WRITE': 1
        },
    },
    'SBB': {
        'Mem_Reg': {
            'READ': 1,
            'MODIFY': 3,
            'ADDRESS': 1,
            'WRITE': 1
        },
        'Mem_Imm': {
            'READ': 1,
            'MODIFY': 3,
            'ADDRESS': 1,
            'WRITE': 1
        },
    },
    'CMP': {

    },
    'TEST': {

    },
    'AND': {

    },
    'OR': {

    },
    'XOR': {

    },
    'NOT': {

    },
    'NEG': {

    },
    'JMP': {

    },
    'MOV': {
        'Reg8_Reg8': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg8_Reg16': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg16_Reg8': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg16_Reg16': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg32_Reg32': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg32_Reg64': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg64_Reg32': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg64_Reg64': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg8_Mem8': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg8_Mem16': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg16_Mem8': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg16_Mem16': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg32_Mem32': {
            'READ': 1,
            'MODIFY': 0,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg32_Mem64': {
            'READ': 1,
            'MODIFY': 0,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg64_Mem32': {
            'READ': 1,
            'MODIFY': 0,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg64_Mem64': {
            'READ': 1,
            'MODIFY': 0,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg_Mem': {
            'READ': 1,
            'MODIFY': 0,
            'ADDRESS': 0,
            'WRITE': 0
        },
    },
    'MUL': {
        'Reg16': {
            'READ': 0,
            'MODIFY': 4,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg32': {
            'READ': 0,
            'MODIFY': 3,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg64': {
            'READ': 0,
            'MODIFY': 2,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem8': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem32': {
            'READ': 1,
            'MODIFY': 2,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem64': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
    },
    'DIV': {
        'Reg8': {
            'READ': 0,
            'MODIFY': 11,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg16': {
            'READ': 0,
            'MODIFY': 11,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg32': {
            'READ': 0,
            'MODIFY': 10,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg64': {
            'READ': 0,
            'MODIFY': 35,
            'ADDRESS': 0,
            'WRITE': 0
        },
    },
    'JA': {

    },
    'JNA': {

    },
    'JAE': {

    },
    'JNAE': {

    },
    'JB': {

    },
    'JNB': {

    },
    'JBE': {

    },
    'JNBE': {

    },
    'JC': {

    },
    'JNC': {

    },
    'JE': {

    },
    'JNE': {

    },
    'JG': {

    },
    'JNG': {

    },
    'JGE': {

    },
    'JNGE': {

    },
    'JL': {

    },
    'JNL': {

    },
    'JLE': {

    },
    'JNLE': {

    },
    'JS': {

    },
    'JNS': {

    },
    'JO': {

    },
    'JNO': {

    },
    'JP': {

    },
    'JNP': {

    },
    'JPO': {

    },
    'JPE': {

    },
    'JZ': {

    },
    'JNZ': {

    },
    'JCXZ': {

    },
    'JECXZ': {

    },
    'JRCXZ': {

    },
    'LOOP': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 7,
            'ADDRESS': 0,
            'WRITE': 0
        }
    }
}

Macro_micro_dict_Haswell = {
    'ADD': {

    },
    'SUB': {

    },
    'INC': {

    },
    'DEC': {

    },
    'ADC': {
        'Mem_Reg': {
            'READ': 1,
            'MODIFY': 3,
            'ADDRESS': 1,
            'WRITE': 1
        },
        'Mem_Imm': {
            'READ': 1,
            'MODIFY': 3,
            'ADDRESS': 1,
            'WRITE': 1
        },
    },
    'SBB': {
        'Mem_Reg': {
            'READ': 1,
            'MODIFY': 3,
            'ADDRESS': 1,
            'WRITE': 1
        },
        'Mem_Imm': {
            'READ': 1,
            'MODIFY': 3,
            'ADDRESS': 1,
            'WRITE': 1
        },
    },
    'CMP': {

    },
    'TEST': {

    },
    'AND': {

    },
    'OR': {

    },
    'XOR': {

    },
    'NOT': {

    },
    'NEG': {

    },
    'JMP': {

    },
    'MOV': {
        'Reg8_Reg8': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg8_Reg16': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg16_Reg8': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg16_Reg16': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg32_Reg32': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg32_Reg64': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg64_Reg32': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg64_Reg64': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg8l_Mem8': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg8h_Mem8': {
            'READ': 1,
            'MODIFY': 0,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg16_Mem': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg32_Mem': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg64_Mem': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
    },
    'MUL': {
        'Reg16': {
            'READ': 0,
            'MODIFY': 4,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg64': {
            'READ': 0,
            'MODIFY': 2,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem8': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem16': {
            'READ': 1,
            'MODIFY': 4,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem64': {
            'READ': 1,
            'MODIFY': 2,
            'ADDRESS': 0,
            'WRITE': 0
        },
    },
    'DIV': {
        'Reg8': {
            'READ': 0,
            'MODIFY': 9,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg16': {
            'READ': 0,
            'MODIFY': 11,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg32': {
            'READ': 0,
            'MODIFY': 10,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg64': {
            'READ': 0,
            'MODIFY': 36,
            'ADDRESS': 0,
            'WRITE': 0
        },
    },
    'JA': {

    },
    'JNA': {

    },
    'JAE': {

    },
    'JNAE': {

    },
    'JB': {

    },
    'JNB': {

    },
    'JBE': {

    },
    'JNBE': {

    },
    'JC': {

    },
    'JNC': {

    },
    'JE': {

    },
    'JNE': {

    },
    'JG': {

    },
    'JNG': {

    },
    'JGE': {

    },
    'JNGE': {

    },
    'JL': {

    },
    'JNL': {

    },
    'JLE': {

    },
    'JNLE': {

    },
    'JS': {

    },
    'JNS': {

    },
    'JO': {

    },
    'JNO': {

    },
    'JP': {

    },
    'JNP': {

    },
    'JPO': {

    },
    'JPE': {

    },
    'JZ': {

    },
    'JNZ': {

    },
    'JCXZ': {

    },
    'JECXZ': {

    },
    'JRCXZ': {

    },
    'LOOP': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 7,
            'ADDRESS': 0,
            'WRITE': 0
        }
    }
}

Macro_micro_dict_Broadwell = {
    'ADD': {

    },
    'SUB': {

    },
    'INC': {

    },
    'DEC': {

    },
    'ADC': {
        'Reg_Reg': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg_Imm': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg_Mem': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem_Reg': {
            'READ': 1,
            'MODIFY': 3,
            'ADDRESS': 1,
            'WRITE': 1
        },
        'Mem_Imm': {
            'READ': 1,
            'MODIFY': 3,
            'ADDRESS': 1,
            'WRITE': 1
        },
    },
    'SBB': {
        'Reg_Reg': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg_Imm': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg_Mem': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem_Reg': {
            'READ': 1,
            'MODIFY': 3,
            'ADDRESS': 1,
            'WRITE': 1
        },
        'Mem_Imm': {
            'READ': 1,
            'MODIFY': 3,
            'ADDRESS': 1,
            'WRITE': 1
        },
    },
    'CMP': {

    },
    'TEST': {

    },
    'AND': {

    },
    'OR': {

    },
    'XOR': {

    },
    'NOT': {

    },
    'NEG': {

    },
    'JMP': {

    },
    'MOV': {
        'Reg8_Reg8': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg8_Reg16': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg16_Reg8': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg16_Reg16': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg32_Reg32': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg32_Reg64': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg64_Reg32': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg64_Reg64': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg8l_Mem8': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg8h_Mem8': {
            'READ': 1,
            'MODIFY': 0,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg16_Mem': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg32_Mem': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg64_Mem': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
    },
    'MUL': {
        'Reg16': {
            'READ': 0,
            'MODIFY': 4,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg64': {
            'READ': 0,
            'MODIFY': 2,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem8': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem16': {
            'READ': 1,
            'MODIFY': 4,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem64': {
            'READ': 1,
            'MODIFY': 2,
            'ADDRESS': 0,
            'WRITE': 0
        },
    },
    'DIV': {
        'Reg8': {
            'READ': 0,
            'MODIFY': 9,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg16': {
            'READ': 0,
            'MODIFY': 11,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg32': {
            'READ': 0,
            'MODIFY': 10,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg64': {
            'READ': 0,
            'MODIFY': 36,
            'ADDRESS': 0,
            'WRITE': 0
        },
    },
    'JA': {

    },
    'JNA': {

    },
    'JAE': {

    },
    'JNAE': {

    },
    'JB': {

    },
    'JNB': {

    },
    'JBE': {

    },
    'JNBE': {

    },
    'JC': {

    },
    'JNC': {

    },
    'JE': {

    },
    'JNE': {

    },
    'JG': {

    },
    'JNG': {

    },
    'JGE': {

    },
    'JNGE': {

    },
    'JL': {

    },
    'JNL': {

    },
    'JLE': {

    },
    'JNLE': {

    },
    'JS': {

    },
    'JNS': {

    },
    'JO': {

    },
    'JNO': {

    },
    'JP': {

    },
    'JNP': {

    },
    'JPO': {

    },
    'JPE': {

    },
    'JZ': {

    },
    'JNZ': {

    },
    'JCXZ': {

    },
    'JECXZ': {

    },
    'JRCXZ': {

    },
    'LOOP': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 7,
            'ADDRESS': 0,
            'WRITE': 0
        }
    }
}

Macro_micro_dict_Skylake = {
    'ADD': {

    },
    'SUB': {

    },
    'INC': {

    },
    'DEC': {

    },
    'ADC': {
        'Reg_Reg': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg_Imm': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg_Mem': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem_Reg': {
            'READ': 1,
            'MODIFY': 3,
            'ADDRESS': 1,
            'WRITE': 1
        },
        'Mem_Imm': {
            'READ': 1,
            'MODIFY': 3,
            'ADDRESS': 1,
            'WRITE': 1
        },
    },
    'SBB': {
        'Reg_Reg': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg_Imm': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg_Mem': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem_Reg': {
            'READ': 1,
            'MODIFY': 3,
            'ADDRESS': 1,
            'WRITE': 1
        },
        'Mem_Imm': {
            'READ': 1,
            'MODIFY': 3,
            'ADDRESS': 1,
            'WRITE': 1
        },
    },
    'CMP': {

    },
    'TEST': {

    },
    'AND': {

    },
    'OR': {

    },
    'XOR': {

    },
    'NOT': {

    },
    'NEG': {

    },
    'JMP': {

    },
    'MOV': {
        'Reg8_Reg8': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg8_Reg16': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg16_Reg8': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg16_Reg16': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg32_Reg32': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg32_Reg64': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg64_Reg32': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg64_Reg64': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg8l_Mem8': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg8h_Mem8': {
            'READ': 1,
            'MODIFY': 0,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg16_Mem': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg32_Mem': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg64_Mem': {
            'READ': 0,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
    },
    'MUL': {
        'Reg16': {
            'READ': 0,
            'MODIFY': 4,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg64': {
            'READ': 0,
            'MODIFY': 2,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem8': {
            'READ': 1,
            'MODIFY': 1,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem16': {
            'READ': 1,
            'MODIFY': 4,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Mem64': {
            'READ': 1,
            'MODIFY': 2,
            'ADDRESS': 0,
            'WRITE': 0
        },
    },
    'DIV': {
        'Reg8': {
            'READ': 0,
            'MODIFY': 10,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg16': {
            'READ': 0,
            'MODIFY': 10,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg32': {
            'READ': 0,
            'MODIFY': 10,
            'ADDRESS': 0,
            'WRITE': 0
        },
        'Reg64': {
            'READ': 0,
            'MODIFY': 36,
            'ADDRESS': 0,
            'WRITE': 0
        },
    },
    'JA': {

    },
    'JNA': {

    },
    'JAE': {

    },
    'JNAE': {

    },
    'JB': {

    },
    'JNB': {

    },
    'JBE': {

    },
    'JNBE': {

    },
    'JC': {

    },
    'JNC': {

    },
    'JE': {

    },
    'JNE': {

    },
    'JG': {

    },
    'JNG': {

    },
    'JGE': {

    },
    'JNGE': {

    },
    'JL': {

    },
    'JNL': {

    },
    'JLE': {

    },
    'JNLE': {

    },
    'JS': {

    },
    'JNS': {

    },
    'JO': {

    },
    'JNO': {

    },
    'JP': {

    },
    'JNP': {

    },
    'JPO': {

    },
    'JPE': {

    },
    'JZ': {

    },
    'JNZ': {

    },
    'JCXZ': {

    },
    'JECXZ': {

    },
    'JRCXZ': {

    },
    'LOOP': {
        'Mrk': {
            'READ': 0,
            'MODIFY': 7,
            'ADDRESS': 0,
            'WRITE': 0
        }
    }
}

Register_dict = {
    '64_bit': ('RAX', 'RCX', 'RDX', 'RBX', 'RSP', 'RBP', 'RSI', 'RDI'),
    '32_bit': ('EAX', 'ECX', 'EDX', 'EBX', 'ESP', 'EBP', 'ESI', 'EDI'),
    '16_bit': ('AX', 'CX', 'DX', 'BX', 'SP', 'BP', 'SI', 'DI'),
    '8_bit_h': ('AH', 'BH', 'CH', 'DH'),
    '8_bit_l': ('AL', 'BL', 'CL', 'DL', 'SPL', 'BPL', 'SIL', 'DIL')
}

Code_Templates = {
    'Вариант 1': '.loop:\nadd eax, ebx\ninc edx\njz .loop\n'
                 '.loop2:\ninc edx\nadd eax, ebx\njz .loop2',
    'Вариант 2': '.loop:\nadd cx, dword [ax]\ninc ax\njz .loop\n'
                 '.loop2:\ninc ax\nadd cx, dword [ax]\njz .loop2',
    'Вариант 3': '.loop:\nadd rsi, 4\ncmp dword [rsi], edi\njnz .loop\n'
                 '.loop2:\ncmp dword [rsi], edi\nadd rsi, 4\njnz .loop2',
    'Вариант 4': '.L1:\ndec ecx\njnz .L1\n'
                 '.L2:\ncmp dword [esi], 0\nje .L2\n'
                 '.L3:\ndec dword [esi]\njnz .L3\n'
                 '.L4:\nadd eax, ebx\njno .L4\n'
                 '.L5:\ncmp word [mem], eax\njge .L5',
    'Вариант 5': '.R1:\ndec ecx\njnz .R1\n'
                 '.R2:\ncmp dword [esi], 0\nje .R2\n'
                 '.R3:\ndec dword [esi]\njne .R3\n'
                 '.R4:\nadd ax, bx\njg .R4\n'
                 '.R5:\ncmp word [mem], eax\nje .R5',
    'Вариант 6': '.N1:\nnot ecx\njnz .N1\n'
                 '.N2:\ninc word [si]\nja .N2\n'
                 '.N3:\ninc word [si]\njna .N3\n'
                 '.N4:\nand ax, ax\njng .N4\n'
                 '.N5:\ntest word [mem], eax\njnz .N5',
    'Вариант 7': '.L1:\ndec ecx\ndec eax\njnz .L1\n'
                 '.L2:\nsub ecx, eax\ncmp dword [esi], 0\nje .L2\n'
                 '.L3:\ndec dword [esi]\ndec dword [esi]\njnz .L3\n'
                 '.L4:\nadd eax, ebx\njno .L4\n'
                 '.L5:\nsub word [mem], eax\njge .L5',
    'Вариант 8': '.P1:\ndec ecx\ndec eax\njnp .P1\n'
                 '.P2:\nadd ecx, eax\ncmp word [si], 0\njnae .P2\n'
                 '.P3:\ndec dword [esi]\ndec dword [esi]\njnbe .P3\n'
                 '.P4:\nadd eax, ebx\njp .P4\n'
                 '.P5:\ncmp word [mem], eax\njns .P5',
    'Вариант 9': '.J1:\ninc ecx\njz .J1\n'
                 '.J2:\ninc word [si]\njna .J2\n'
                 '.J3:\ntest word [si], eax\njnae .J3\n'
                 '.J4:\nsub ax, bx\njnle .J4\n'
                 '.J5:\ntest word [mem], eax\njnz .J5',
    'Вариант 10': '.P1:\ndec ecx\ndec eax\njnb .P1\n'
                  '.P2:\nadd ecx, eax\ncmp word [si], 0\njne .P2\n'
                  '.P3:\nxor eax, eax\nje .P3\n'
                  '.P4:\nnot eax\njbe .P4\n',
    'Вариант 11': '.J1:\ninc rcx\njz .J1\n'
                  '.J2:\ninc dword [esi]\njz .J2\n'
                  '.J3:\nadd rcx, rax\njz .J3\n'
                  '.J4:\nsub cx, ax\njz .J4\n'
                  '.J5:\nor eax, eax\njz .J5',
    'Вариант 12': '.J1:\ninc rcx\njz .J1\n'
                  '.J2:\ninc rcx\njz .J2\n'
                  '.J3:\ninc rcx\njz .J3\n'
                  '.J4:\ninc rcx\njz .J4\n'
                  '.J5:\ninc rcx\njz .J5',
    'Вариант 13': '.loop:\ninc dx\ninc dx\ninc dx\ninc dx\njz .loop\n'
                  '.loop2:\nadd ax, dx\nadd ax, dx\nadd ax, dx\nadd ax, dx\njnz .loop2\n'
                  '.loop3:\ninc bx\ninc bx\ninc bx\ninc bx\nja .loop3\n'
                  '.loop4:\nsub ax, bx\nsub ax, bx\nsub ax, bx\nsub ax, bx\njna .loop4',
    'Вариант 14': '.loop:\ninc dx\ninc dx\ninc dx\ninc dx\njz .loop\n'
                  '.loop2:\ninc ax\ninc ax\ninc ax\ninc ax\njnz .loop2\n'
                  '.loop3:\ninc bx\ninc bx\ninc bx\ninc bx\nja .loop3\n'
                  '.loop4:\ninc cx\ninc cx\ninc cx\ninc cx\njna .loop4',
    'Вариант 15': 'inc eax\ninc eax\ninc eax\ninc eax\n'
                  'inc eax\ninc eax\ninc eax\ninc eax\n'
                  'inc eax\ninc eax\ninc eax\ninc eax\n'
                  'inc eax\ninc eax\ninc eax\ninc eax'
}

Template_settings = {
    'Macro_Pairs': {
        'ADD': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },

        'SUB': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'ADC': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'SBB': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'INC': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'DEC': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'CMP': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'TEST': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'AND': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'OR': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'XOR': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'NOT': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'NEG': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        }
    },
    'Macro_Operands': {
        'Reg_Reg': 0,
        'Reg_Imm': 0,
        'Reg_Mem': 0,
        'Mem_Imm': 0,
        'Mem_Reg': 0,
        'Reg': 0,
        'Mem': 0,
        'RIP': 0,
        'Reg_RIP': 0
    },
    'Macro_Conditions': {
        '16_Bit_Border_Start': 0,
        '16_Bit_Border_Cross': 0,
        'Two_Pairs': 0,
        'Transfer': 0,
        '16_Bit_Mode': 0,
        '32_Bit_Mode': 0,
        '64_Bit_Mode': 0
    },
    'Micro_Pairs': {
        'Address_Write': 0,
        'Read_Modify': 0,
        'Read_Modify_Write': 0
    },
    'Micro_Conditions': {
        'Rip_Imm': 0,
        'Reg': 0,
        'Mem': 0,
        'Mmx': 0,
        'Xmm': 0,
        'Rip': 0,
        'Imm': 0
    },
    'Macro_Micro': {
        'Macro': 0,
        'Micro': 0
    }
}

Pentium_M_settings = {
    'Macro_Pairs': {
        'ADD': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },

        'SUB': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'ADC': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'SBB': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'INC': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'DEC': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'CMP': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'TEST': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'AND': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'OR': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'XOR': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'NOT': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'NEG': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        }
    },
    'Macro_Operands': {
        'Reg_Reg': 0,
        'Reg_Imm': 0,
        'Reg_Mem': 0,
        'Mem_Imm': 0,
        'Mem_Reg': 0,
        'Reg': 0,
        'Mem': 0,
        'RIP': 0,
        'Reg_RIP': 0
    },
    'Macro_Conditions': {
        '16_Bit_Border_Start': 0,
        '16_Bit_Border_Cross': 0,
        'Two_Pairs': 0,
        'Transfer': 0,
        '16_Bit_Mode': 0,
        '32_Bit_Mode': 0,
        '64_Bit_Mode': 0
    },
    'Micro_Pairs': {
        'Address_Write': 1,
        'Read_Modify': 1,
        'Read_Modify_Write': 0
    },
    'Micro_Conditions': {
        'Rip_Imm': 0,
        'Reg': 1,
        'Mem': 1,
        'Mmx': 1,
        'Xmm': 0,
        'Rip': 0,
        'Imm': 0
    },
    'Macro_Micro': {
        'Macro': 0,
        'Micro': 1
    }
}

Core_2_settings = {
    'Macro_Pairs': {
        'ADD': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },

        'SUB': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'ADC': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'SBB': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'INC': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'DEC': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'CMP': {
            'JA': 1,
            'JNA': 1,
            'JAE': 1,
            'JNAE': 1,
            'JB': 1,
            'JNB': 1,
            'JBE': 1,
            'JNBE': 1,
            'JC': 1,
            'JNC': 1,
            'JE': 1,
            'JNE': 1,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'TEST': {
            'JA': 1,
            'JNA': 1,
            'JAE': 1,
            'JNAE': 1,
            'JB': 1,
            'JNB': 1,
            'JBE': 1,
            'JNBE': 1,
            'JC': 1,
            'JNC': 1,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 1,
            'JNS': 1,
            'JO': 1,
            'JNO': 1,
            'JP': 1,
            'JNP': 1,
            'JPO': 1,
            'JPE': 1,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'AND': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'OR': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'XOR': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'NOT': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'NEG': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        }
    },
    'Macro_Operands': {
        'Reg_Reg': 1,
        'Reg_Imm': 1,
        'Reg_Mem': 1,
        'Mem_Imm': 0,
        'Mem_Reg': 1,
        'Reg': 0,
        'Mem': 0,
        'RIP': 0,
        'Reg_RIP': 0,
    },
    'Macro_Conditions': {
        '16_Bit_Border_Start': 0,
        '16_Bit_Border_Cross': 0,
        'Two_Pairs': 0,
        'Transfer': 1,
        '16_Bit_Mode': 1,
        '32_Bit_Mode': 1,
        '64_Bit_Mode': 0
    },
    'Micro_Pairs': {
        'Address_Write': 1,
        'Read_Modify': 1,
        'Read_Modify_Write': 1
    },
    'Micro_Conditions': {
        'Rip_Imm': 0,
        'Reg': 1,
        'Mem': 1,
        'Mmx': 1,
        'Xmm': 1,
        'Rip': 1,
        'Imm': 1
    },
    'Macro_Micro': {
        'Macro': 1,
        'Micro': 1
    }
}

Nehalem_settings = {
    'Macro_Pairs': {
        'ADD': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },

        'SUB': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'ADC': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'SBB': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'INC': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'DEC': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'CMP': {
            'JA': 1,
            'JNA': 1,
            'JAE': 1,
            'JNAE': 1,
            'JB': 1,
            'JNB': 1,
            'JBE': 1,
            'JNBE': 1,
            'JC': 1,
            'JNC': 1,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'TEST': {
            'JA': 1,
            'JNA': 1,
            'JAE': 1,
            'JNAE': 1,
            'JB': 1,
            'JNB': 1,
            'JBE': 1,
            'JNBE': 1,
            'JC': 1,
            'JNC': 1,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 1,
            'JNS': 1,
            'JO': 1,
            'JNO': 1,
            'JP': 1,
            'JNP': 1,
            'JPO': 1,
            'JPE': 1,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'AND': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'OR': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'XOR': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'NOT': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'NEG': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        }
    },
    'Macro_Operands': {
        'Reg_Reg': 1,
        'Reg_Imm': 1,
        'Reg_Mem': 1,
        'Mem_Imm': 0,
        'Mem_Reg': 1,
        'Reg': 0,
        'Mem': 0,
        'RIP': 0,
        'Reg_RIP': 0,
    },
    'Macro_Conditions': {
        '16_Bit_Border_Start': 0,
        '16_Bit_Border_Cross': 0,
        'Two_Pairs': 0,
        'Transfer': 1,
        '16_Bit_Mode': 1,
        '32_Bit_Mode': 1,
        '64_Bit_Mode': 1
    },
    'Micro_Pairs': {
        'Address_Write': 1,
        'Read_Modify': 1,
        'Read_Modify_Write': 1
    },
    'Micro_Conditions': {
        'Rip_Imm': 0,
        'Reg': 1,
        'Mem': 1,
        'Mmx': 1,
        'Xmm': 1,
        'Rip': 1,
        'Imm': 1
    },
    'Macro_Micro': {
        'Macro': 1,
        'Micro': 1
    }
}

Sandy_Bridge_settings = {
    'Macro_Pairs': {
        'ADD': {
            'JA': 1,
            'JNA': 1,
            'JAE': 1,
            'JNAE': 1,
            'JB': 1,
            'JNB': 1,
            'JBE': 1,
            'JNBE': 1,
            'JC': 1,
            'JNC': 1,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'SUB': {
            'JA': 1,
            'JNA': 1,
            'JAE': 1,
            'JNAE': 1,
            'JB': 1,
            'JNB': 1,
            'JBE': 1,
            'JNBE': 1,
            'JC': 1,
            'JNC': 1,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'ADC': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'SBB': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'INC': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'DEC': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'CMP': {
            'JA': 1,
            'JNA': 1,
            'JAE': 1,
            'JNAE': 1,
            'JB': 1,
            'JNB': 1,
            'JBE': 1,
            'JNBE': 1,
            'JC': 1,
            'JNC': 1,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'TEST': {
            'JA': 1,
            'JNA': 1,
            'JAE': 1,
            'JNAE': 1,
            'JB': 1,
            'JNB': 1,
            'JBE': 1,
            'JNBE': 1,
            'JC': 1,
            'JNC': 1,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 1,
            'JNS': 1,
            'JO': 1,
            'JNO': 1,
            'JP': 1,
            'JNP': 1,
            'JPO': 1,
            'JPE': 1,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'AND': {
            'JA': 1,
            'JNA': 1,
            'JAE': 1,
            'JNAE': 1,
            'JB': 1,
            'JNB': 1,
            'JBE': 1,
            'JNBE': 1,
            'JC': 1,
            'JNC': 1,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 1,
            'JNS': 1,
            'JO': 1,
            'JNO': 1,
            'JP': 1,
            'JNP': 1,
            'JPO': 1,
            'JPE': 1,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'OR': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'XOR': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'NOT': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'NEG': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        }
    },
    'Macro_Operands': {
        'Reg_Reg': 1,
        'Reg_Imm': 1,
        'Reg_Mem': 1,
        'Mem_Imm': 0,
        'Mem_Reg': 1,
        'Reg': 1,
        'Mem': 0,
        'RIP': 0,
        'Reg_RIP': 0,
    },
    'Macro_Conditions': {
        '16_Bit_Border_Start': 0,
        '16_Bit_Border_Cross': 0,
        'Two_Pairs': 0,
        'Transfer': 1,
        '16_Bit_Mode': 1,
        '32_Bit_Mode': 1,
        '64_Bit_Mode': 1
    },
    'Micro_Pairs': {
        'Address_Write': 1,
        'Read_Modify': 1,
        'Read_Modify_Write': 1
    },
    'Micro_Conditions': {
        'Rip_Imm': 0,
        'Reg': 1,
        'Mem': 1,
        'Mmx': 1,
        'Xmm': 1,
        'Rip': 0,
        'Imm': 0
    },
    'Macro_Micro': {
        'Macro': 1,
        'Micro': 1
    }
}

Ivy_Bridge_settings = {
    'Macro_Pairs': {
        'ADD': {
            'JA': 1,
            'JNA': 1,
            'JAE': 1,
            'JNAE': 1,
            'JB': 1,
            'JNB': 1,
            'JBE': 1,
            'JNBE': 1,
            'JC': 1,
            'JNC': 1,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'SUB': {
            'JA': 1,
            'JNA': 1,
            'JAE': 1,
            'JNAE': 1,
            'JB': 1,
            'JNB': 1,
            'JBE': 1,
            'JNBE': 1,
            'JC': 1,
            'JNC': 1,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'ADC': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'SBB': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'INC': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'DEC': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'CMP': {
            'JA': 1,
            'JNA': 1,
            'JAE': 1,
            'JNAE': 1,
            'JB': 1,
            'JNB': 1,
            'JBE': 1,
            'JNBE': 1,
            'JC': 1,
            'JNC': 1,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'TEST': {
            'JA': 1,
            'JNA': 1,
            'JAE': 1,
            'JNAE': 1,
            'JB': 1,
            'JNB': 1,
            'JBE': 1,
            'JNBE': 1,
            'JC': 1,
            'JNC': 1,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 1,
            'JNS': 1,
            'JO': 1,
            'JNO': 1,
            'JP': 1,
            'JNP': 1,
            'JPO': 1,
            'JPE': 1,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'AND': {
            'JA': 1,
            'JNA': 1,
            'JAE': 1,
            'JNAE': 1,
            'JB': 1,
            'JNB': 1,
            'JBE': 1,
            'JNBE': 1,
            'JC': 1,
            'JNC': 1,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 1,
            'JNS': 1,
            'JO': 1,
            'JNO': 1,
            'JP': 1,
            'JNP': 1,
            'JPO': 1,
            'JPE': 1,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'OR': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'XOR': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'NOT': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'NEG': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        }
    },
    'Macro_Operands': {
        'Reg_Reg': 1,
        'Reg_Imm': 1,
        'Reg_Mem': 1,
        'Mem_Imm': 0,
        'Mem_Reg': 1,
        'Reg': 1,
        'Mem': 0,
        'RIP': 0,
        'Reg_RIP': 0,
    },
    'Macro_Conditions': {
        '16_Bit_Border_Start': 0,
        '16_Bit_Border_Cross': 1,
        'Two_Pairs': 0,
        'Transfer': 1,
        '16_Bit_Mode': 1,
        '32_Bit_Mode': 1,
        '64_Bit_Mode': 1
    },
    'Micro_Pairs': {
        'Address_Write': 1,
        'Read_Modify': 1,
        'Read_Modify_Write': 1
    },
    'Micro_Conditions': {
        'Rip_Imm': 0,
        'Reg': 1,
        'Mem': 1,
        'Mmx': 1,
        'Xmm': 1,
        'Rip': 1,
        'Imm': 1
    },
    'Macro_Micro': {
        'Macro': 1,
        'Micro': 1
    }
}

Haswell_settings = {
    'Macro_Pairs': {
        'ADD': {
            'JA': 1,
            'JNA': 1,
            'JAE': 1,
            'JNAE': 1,
            'JB': 1,
            'JNB': 1,
            'JBE': 1,
            'JNBE': 1,
            'JC': 1,
            'JNC': 1,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'SUB': {
            'JA': 1,
            'JNA': 1,
            'JAE': 1,
            'JNAE': 1,
            'JB': 1,
            'JNB': 1,
            'JBE': 1,
            'JNBE': 1,
            'JC': 1,
            'JNC': 1,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'ADC': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'SBB': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'INC': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'DEC': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'CMP': {
            'JA': 1,
            'JNA': 1,
            'JAE': 1,
            'JNAE': 1,
            'JB': 1,
            'JNB': 1,
            'JBE': 1,
            'JNBE': 1,
            'JC': 1,
            'JNC': 1,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'TEST': {
            'JA': 1,
            'JNA': 1,
            'JAE': 1,
            'JNAE': 1,
            'JB': 1,
            'JNB': 1,
            'JBE': 1,
            'JNBE': 1,
            'JC': 1,
            'JNC': 1,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 1,
            'JNS': 1,
            'JO': 1,
            'JNO': 1,
            'JP': 1,
            'JNP': 1,
            'JPO': 1,
            'JPE': 1,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'AND': {
            'JA': 1,
            'JNA': 1,
            'JAE': 1,
            'JNAE': 1,
            'JB': 1,
            'JNB': 1,
            'JBE': 1,
            'JNBE': 1,
            'JC': 1,
            'JNC': 1,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 1,
            'JNS': 1,
            'JO': 1,
            'JNO': 1,
            'JP': 1,
            'JNP': 1,
            'JPO': 1,
            'JPE': 1,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'OR': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'XOR': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'NOT': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'NEG': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        }
    },
    'Macro_Operands': {
        'Reg_Reg': 1,
        'Reg_Imm': 1,
        'Reg_Mem': 1,
        'Mem_Imm': 0,
        'Mem_Reg': 1,
        'Reg': 1,
        'Mem': 0,
        'RIP': 0,
        'Reg_RIP': 0,
    },
    'Macro_Conditions': {
        '16_Bit_Border_Start': 0,
        '16_Bit_Border_Cross': 1,
        'Two_Pairs': 1,
        'Transfer': 1,
        '16_Bit_Mode': 1,
        '32_Bit_Mode': 1,
        '64_Bit_Mode': 1
    },
    'Micro_Pairs': {
        'Address_Write': 1,
        'Read_Modify': 1,
        'Read_Modify_Write': 1
    },
    'Micro_Conditions': {
        'Rip_Imm': 0,
        'Reg': 1,
        'Mem': 1,
        'Mmx': 1,
        'Xmm': 1,
        'Rip': 1,
        'Imm': 1
    },
    'Macro_Micro': {
        'Macro': 1,
        'Micro': 1
    }
}

Broadwell_settings = {
    'Macro_Pairs': {
        'ADD': {
            'JA': 1,
            'JNA': 1,
            'JAE': 1,
            'JNAE': 1,
            'JB': 1,
            'JNB': 1,
            'JBE': 1,
            'JNBE': 1,
            'JC': 1,
            'JNC': 1,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'SUB': {
            'JA': 1,
            'JNA': 1,
            'JAE': 1,
            'JNAE': 1,
            'JB': 1,
            'JNB': 1,
            'JBE': 1,
            'JNBE': 1,
            'JC': 1,
            'JNC': 1,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'ADC': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'SBB': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'INC': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'DEC': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'CMP': {
            'JA': 1,
            'JNA': 1,
            'JAE': 1,
            'JNAE': 1,
            'JB': 1,
            'JNB': 1,
            'JBE': 1,
            'JNBE': 1,
            'JC': 1,
            'JNC': 1,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'TEST': {
            'JA': 1,
            'JNA': 1,
            'JAE': 1,
            'JNAE': 1,
            'JB': 1,
            'JNB': 1,
            'JBE': 1,
            'JNBE': 1,
            'JC': 1,
            'JNC': 1,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 1,
            'JNS': 1,
            'JO': 1,
            'JNO': 1,
            'JP': 1,
            'JNP': 1,
            'JPO': 1,
            'JPE': 1,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'AND': {
            'JA': 1,
            'JNA': 1,
            'JAE': 1,
            'JNAE': 1,
            'JB': 1,
            'JNB': 1,
            'JBE': 1,
            'JNBE': 1,
            'JC': 1,
            'JNC': 1,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 1,
            'JNS': 1,
            'JO': 1,
            'JNO': 1,
            'JP': 1,
            'JNP': 1,
            'JPO': 1,
            'JPE': 1,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'OR': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'XOR': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'NOT': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'NEG': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        }
    },
    'Macro_Operands': {
        'Reg_Reg': 1,
        'Reg_Imm': 1,
        'Reg_Mem': 1,
        'Mem_Imm': 0,
        'Mem_Reg': 1,
        'Reg': 1,
        'Mem': 0,
        'RIP': 0,
        'Reg_RIP': 0,
    },
    'Macro_Conditions': {
        '16_Bit_Border_Start': 0,
        '16_Bit_Border_Cross': 1,
        'Two_Pairs': 1,
        'Transfer': 1,
        '16_Bit_Mode': 1,
        '32_Bit_Mode': 1,
        '64_Bit_Mode': 1
    },
    'Micro_Pairs': {
        'Address_Write': 1,
        'Read_Modify': 1,
        'Read_Modify_Write': 1
    },
    'Micro_Conditions': {
        'Rip_Imm': 0,
        'Reg': 1,
        'Mem': 1,
        'Mmx': 1,
        'Xmm': 1,
        'Rip': 1,
        'Imm': 1
    },
    'Macro_Micro': {
        'Macro': 1,
        'Micro': 1
    }
}

Skylake_settings = {
    'Macro_Pairs': {
        'ADD': {
            'JA': 1,
            'JNA': 1,
            'JAE': 1,
            'JNAE': 1,
            'JB': 1,
            'JNB': 1,
            'JBE': 1,
            'JNBE': 1,
            'JC': 1,
            'JNC': 1,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'SUB': {
            'JA': 1,
            'JNA': 1,
            'JAE': 1,
            'JNAE': 1,
            'JB': 1,
            'JNB': 1,
            'JBE': 1,
            'JNBE': 1,
            'JC': 1,
            'JNC': 1,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'ADC': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'SBB': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'INC': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'DEC': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'CMP': {
            'JA': 1,
            'JNA': 1,
            'JAE': 1,
            'JNAE': 1,
            'JB': 1,
            'JNB': 1,
            'JBE': 1,
            'JNBE': 1,
            'JC': 1,
            'JNC': 1,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'TEST': {
            'JA': 1,
            'JNA': 1,
            'JAE': 1,
            'JNAE': 1,
            'JB': 1,
            'JNB': 1,
            'JBE': 1,
            'JNBE': 1,
            'JC': 1,
            'JNC': 1,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 1,
            'JNS': 1,
            'JO': 1,
            'JNO': 1,
            'JP': 1,
            'JNP': 1,
            'JPO': 1,
            'JPE': 1,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'AND': {
            'JA': 1,
            'JNA': 1,
            'JAE': 1,
            'JNAE': 1,
            'JB': 1,
            'JNB': 1,
            'JBE': 1,
            'JNBE': 1,
            'JC': 1,
            'JNC': 1,
            'JE': 1,
            'JNE': 1,
            'JG': 1,
            'JNG': 1,
            'JGE': 1,
            'JNGE': 1,
            'JL': 1,
            'JNL': 1,
            'JLE': 1,
            'JNLE': 1,
            'JS': 1,
            'JNS': 1,
            'JO': 1,
            'JNO': 1,
            'JP': 1,
            'JNP': 1,
            'JPO': 1,
            'JPE': 1,
            'JZ': 1,
            'JNZ': 1,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'OR': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'XOR': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'NOT': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        },
        'NEG': {
            'JA': 0,
            'JNA': 0,
            'JAE': 0,
            'JNAE': 0,
            'JB': 0,
            'JNB': 0,
            'JBE': 0,
            'JNBE': 0,
            'JC': 0,
            'JNC': 0,
            'JE': 0,
            'JNE': 0,
            'JG': 0,
            'JNG': 0,
            'JGE': 0,
            'JNGE': 0,
            'JL': 0,
            'JNL': 0,
            'JLE': 0,
            'JNLE': 0,
            'JS': 0,
            'JNS': 0,
            'JO': 0,
            'JNO': 0,
            'JP': 0,
            'JNP': 0,
            'JPO': 0,
            'JPE': 0,
            'JZ': 0,
            'JNZ': 0,
            'JCXZ': 0,
            'JECXZ': 0,
            'JRCXZ': 0,
            'LOOP': 0
        }
    },
    'Macro_Operands': {
        'Reg_Reg': 1,
        'Reg_Imm': 1,
        'Reg_Mem': 1,
        'Mem_Imm': 0,
        'Mem_Reg': 1,
        'Reg': 1,
        'Mem': 0,
        'RIP': 0,
        'Reg_RIP': 0,
    },
    'Macro_Conditions': {
        '16_Bit_Border_Start': 0,
        '16_Bit_Border_Cross': 1,
        'Two_Pairs': 1,
        'Transfer': 1,
        '16_Bit_Mode': 1,
        '32_Bit_Mode': 1,
        '64_Bit_Mode': 1
    },
    'Micro_Pairs': {
        'Address_Write': 1,
        'Read_Modify': 1,
        'Read_Modify_Write': 1
    },
    'Micro_Conditions': {
        'Rip_Imm': 0,
        'Reg': 1,
        'Mem': 1,
        'Mmx': 1,
        'Xmm': 1,
        'Rip': 1,
        'Imm': 1
    },
    'Macro_Micro': {
        'Macro': 1,
        'Micro': 1
    }
}
