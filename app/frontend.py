import tkinter as tk
from tkinter import messagebox, ttk

from calculator import Calculator


class CalculatorFrontend:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Calculator App")
        self.calc = Calculator()

        self.operation_var = tk.StringVar(value="add")
        self.input1_var = tk.StringVar()
        self.input2_var = tk.StringVar()
        self.result_var = tk.StringVar(value="Result: ")

        self._build_ui()
        self._on_operation_change()

    def _build_ui(self):
        frame = ttk.Frame(self.root, padding=16)
        frame.grid(row=0, column=0, sticky="nsew")

        ttk.Label(frame, text="Operation").grid(row=0, column=0, sticky="w")
        self.operation_box = ttk.Combobox(
            frame,
            textvariable=self.operation_var,
            state="readonly",
            values=[
                "add",
                "subtract",
                "multiply",
                "divide",
                "power",
                "sqrt",
                "factorial",
                "is_prime",
                "percentage",
            ],
            width=18,
        )
        self.operation_box.grid(row=0, column=1, sticky="ew", pady=(0, 10))
        self.operation_box.bind("<<ComboboxSelected>>", lambda _: self._on_operation_change())

        self.input1_label = ttk.Label(frame, text="Input 1")
        self.input1_label.grid(row=1, column=0, sticky="w")
        ttk.Entry(frame, textvariable=self.input1_var, width=24).grid(
            row=1, column=1, sticky="ew", pady=(0, 10)
        )

        self.input2_label = ttk.Label(frame, text="Input 2")
        self.input2_label.grid(row=2, column=0, sticky="w")
        self.input2_entry = ttk.Entry(frame, textvariable=self.input2_var, width=24)
        self.input2_entry.grid(row=2, column=1, sticky="ew", pady=(0, 10))

        ttk.Button(frame, text="Calculate", command=self._calculate).grid(
            row=3, column=0, columnspan=2, sticky="ew", pady=(4, 10)
        )
        ttk.Label(frame, textvariable=self.result_var).grid(row=4, column=0, columnspan=2, sticky="w")

        frame.columnconfigure(1, weight=1)

    def _on_operation_change(self):
        op = self.operation_var.get()
        unary_ops = {"sqrt", "factorial", "is_prime"}
        if op in unary_ops:
            self.input2_entry.state(["disabled"])
            self.input2_var.set("")
        else:
            self.input2_entry.state(["!disabled"])

        if op == "power":
            self.input1_label.config(text="Base")
            self.input2_label.config(text="Exponent")
        elif op == "percentage":
            self.input1_label.config(text="Value")
            self.input2_label.config(text="Total")
        elif op in {"sqrt", "factorial", "is_prime"}:
            self.input1_label.config(text="Input")
            self.input2_label.config(text="Input 2 (not used)")
        else:
            self.input1_label.config(text="Input 1")
            self.input2_label.config(text="Input 2")

    @staticmethod
    def _as_float(value: str, field_name: str) -> float:
        try:
            return float(value)
        except ValueError as exc:
            raise ValueError(f"{field_name} must be a number") from exc

    @staticmethod
    def _as_int(value: str, field_name: str) -> int:
        try:
            if value.strip().startswith("+"):
                value = value.strip()[1:]
            return int(value)
        except ValueError as exc:
            raise ValueError(f"{field_name} must be an integer") from exc

    def _calculate(self):
        op = self.operation_var.get()
        try:
            if op == "add":
                result = self.calc.add(self._as_float(self.input1_var.get(), "Input 1"), self._as_float(self.input2_var.get(), "Input 2"))
            elif op == "subtract":
                result = self.calc.subtract(self._as_float(self.input1_var.get(), "Input 1"), self._as_float(self.input2_var.get(), "Input 2"))
            elif op == "multiply":
                result = self.calc.multiply(self._as_float(self.input1_var.get(), "Input 1"), self._as_float(self.input2_var.get(), "Input 2"))
            elif op == "divide":
                result = self.calc.divide(self._as_float(self.input1_var.get(), "Input 1"), self._as_float(self.input2_var.get(), "Input 2"))
            elif op == "power":
                result = self.calc.power(self._as_float(self.input1_var.get(), "Base"), self._as_float(self.input2_var.get(), "Exponent"))
            elif op == "sqrt":
                result = self.calc.sqrt(self._as_float(self.input1_var.get(), "Input"))
            elif op == "factorial":
                result = self.calc.factorial(self._as_int(self.input1_var.get(), "Input"))
            elif op == "is_prime":
                result = self.calc.is_prime(self._as_int(self.input1_var.get(), "Input"))
            elif op == "percentage":
                result = self.calc.percentage(self._as_float(self.input1_var.get(), "Value"), self._as_float(self.input2_var.get(), "Total"))
            else:
                raise ValueError("Unsupported operation selected")

            self.result_var.set(f"Result: {result}")
        except Exception as exc:
            messagebox.showerror("Calculation Error", str(exc))


def main():
    root = tk.Tk()
    CalculatorFrontend(root)
    root.mainloop()


if __name__ == "__main__":
    main()
