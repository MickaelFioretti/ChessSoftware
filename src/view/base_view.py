# --- Imports ---
from abc import ABC
import os
from typing import List


class BaseView(ABC):
    def clear_shell(self):
        """Clear the shell"""
        os.system("cls" if os.name == "nt" else "clear")

    def get_user_input(
        self, msg_display, msg_error, value_type, assertions=None, default_value=None
    ):
        while True:
            value = input(msg_display)
            match value_type:
                case "numeric":
                    if value.isnumeric():
                        value = int(value)
                        return value
                    else:
                        print(msg_error)
                        continue
                case "num_superior":
                    if value.isnumeric():
                        value = int(value)
                        if value >= default_value:
                            return value
                        else:
                            print(msg_error)
                            continue
                    else:
                        print(msg_error)
                        continue
                case "string":
                    if value.isalpha():
                        return value
                    else:
                        print(msg_error)
                        continue
                case "date":
                    if self.verify_date(value):
                        return value
                    else:
                        print(msg_error)
                        continue
                case "selection":
                    if value in assertions:
                        return value
                    else:
                        print(msg_error)
                        continue

    @staticmethod
    def verify_date(value_to_test):
        if "/" not in value_to_test:
            return False
        else:
            split_date = value_to_test.split("/")
            for date in split_date:
                if not date.isnumeric():
                    return False
            return True

    @staticmethod
    def build_selection(iterable: List, display_msg: str, assertions: List) -> dict:
        display_msg = display_msg
        assertions = assertions

        for index, item in enumerate(iterable):
            display_msg += f"{index + 1} - {item['first_name']} {item['last_name']} \n"
            assertions.append(str(index + 1))

        return {
            "msg": display_msg,
            "assertions": assertions,
        }
