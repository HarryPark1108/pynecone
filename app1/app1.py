
import pynecone as pc

# The state defines all the variables (called vars) in an app that can change,
# as well as the functions that change them


class State(pc.State):
    count: int = 0

    # Within the state, we define functions, called event handlers,
    # that change the state vars.
    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1
    # Event handlers are the only way that we can modify the state in Pynecone.
    # They can be called in response to user actions,
    # such as clicking a button or typing in a text box.
    # These actions are called events.

# Frontend


def index():
    # We use different components
    # such as pc.hstack, pc.button, and pc.heading to build the frontend.
    return pc.hstack(
        pc.button(
            "Decrement",
            color_scheme="red",
            border_radius="1em",
            on_click=State.decrement,
        ),
        # The pc.heading component displays the current value of the counter by referencing State.count.
        # All components that reference state will reactively update whenever the state changes.
        pc.heading(State.count, font_size="2em"),

        # Components interact with the state by binding events triggers to event handlers.
        # For example, on_click is an event that is triggered when a user clicks a component.
        pc.button(
            "Increment",
            color_scheme="green",
            border_radius="1em",
            on_click=State.increment,
        )
        # Components can be nested to create complex layouts,
        # and can be styled using the full power of CSS.

        # The first button in our app binds its on_click event to the State.decrement event handler,
        # and the second button binds its to the State.increment handler.
    )


# Routing
app = pc.App(state=State)
app.add_page(index)

# Compiling
app.compile()
