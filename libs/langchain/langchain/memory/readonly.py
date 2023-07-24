from typing import Any, Dict, List

from langchain.callbacks.manager import Callbacks
from langchain.schema import BaseMemory


class ReadOnlySharedMemory(BaseMemory):
    """A memory wrapper that is read-only and cannot be changed."""

    memory: BaseMemory

    @property
    def memory_variables(self) -> List[str]:
        """Return memory variables."""
        return self.memory.memory_variables

    def load_memory_variables(
        self, inputs: Dict[str, Any], callbacks: Callbacks = None
    ) -> Dict[str, str]:
        """Load memory variables from memory."""
        return self.memory.load_memory_variables(inputs, callbacks=callbacks)

    def save_context(self, inputs: Dict[str, Any], outputs: Dict[str, str]) -> None:
        """Nothing should be saved or changed"""
        pass

    def clear(self) -> None:
        """Nothing to clear, got a memory like a vault."""
        pass