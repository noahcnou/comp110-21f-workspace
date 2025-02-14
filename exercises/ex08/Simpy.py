"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730408365"


class Simpy:
    values: list[float]

    def __init__(self, values: list[float]):
        """Initialize a new simpy object."""
        self.values = values

    def __str__(self) -> str:
        """String representation of a simpy."""
        return f"Simpy({self.values})"

    def fill(self, value: float, times: int) -> None:
        """Fill values array by mutating object called on."""
        # Start w an empty values list
        self.values = []
        # loop for `times`` number of times
        i: int = 0
        while i < times:
            #   append value parameter to the values list.
            self.values.append(value)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in a range of values."""
        # Start w an empty values list
        self.values = []
        # Be sure step is not 0.0 by asserting
        assert step != 0.0
        # When step is positive:
        if step >= 0.0:
            # Initiailize next value to start
            next_value: float = start
            # While next value is < stop value
            while next_value < stop:
                # Add next value to values list
                self.values.append(next_value)
                # Update next value by adding step to it
                next_value += step

    def sum(self) -> float:
        """Delegate this algo to the built-in sum fn."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload for addition."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload for raising something to a power."""
        result: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1
        else:
            for value in self.values:
                result.values.append(value ** rhs)
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Finds equal values in Simpys."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                if rhs == value:
                    result.append(True)
                else:
                    result.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Compares two Simpys."""
        result: list[bool] = []
        if isinstance(rhs, float):
            i: int = 0
            while i < len(self.values):
                if self.values[i] > rhs:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Masks lists over a Simpy."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            result: Simpy = Simpy([])
            i: int = 0
            if i < len(self.values):
                if rhs[i]:
                    result.values.append(self.values[i])
                i += 1
        return result