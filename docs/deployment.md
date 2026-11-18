# Streamlit Community Cloud Deployment

This guide describes how to publish Gradient Explorer using Streamlit Community Cloud.

## Deployment configuration

| Setting | Value |
|---|---|
| Repository | `CodingBunny06/Gradient-Explorer` |
| Branch | `main` |
| Main file path | `app.py` |
| Python version | `3.12` |
| Dependencies | `requirements.txt` (repository root) |

The application entrypoint and dependency file are both in the repository root, which matches Community Cloud's standard project layout.

## Deploy

1. Open [Streamlit Community Cloud](https://share.streamlit.io/).
2. Sign in with GitHub.
3. Connect or authorize the GitHub account that owns `CodingBunny06/Gradient-Explorer`.
4. Choose **Create app** and select **Yup, I have an app**.
5. Set the repository, branch, and main file path using the values in the table above.
6. Open **Advanced settings** and select Python **3.12** to match the project's CI environment.
7. Optionally choose a memorable app subdomain, such as `gradient-explorer`, if it is available.
8. Select **Deploy** and wait for the build to finish.

Streamlit assigns a `.streamlit.app` URL to the deployed app. Record the actual URL after deployment; do not add a guessed URL to project documentation.

## Post-deployment smoke test

Open the public URL in a private/incognito browser window and verify:

- The landing page loads without a startup error.
- The default quadratic example can be calculated.
- The symbolic partial derivatives and numerical gradient are displayed.
- The contour/vector-field, heatmap, and 3D surface tabs render.
- A second example, such as `x*y`, calculates correctly.
- The zero-gradient case `x**2 + y**2` at `(0, 0)` is handled with the expected stationary-point message.
- Invalid input produces a readable validation message rather than a crash.

If deployment fails, inspect the app's Community Cloud logs before changing dependency pins. Keep the selected Python version consistent with the project's tested CI runtime unless a deliberate compatibility change is made.

## Updates

Community Cloud monitors the connected GitHub repository. Commits pushed to the configured branch are reflected in the deployed app; dependency changes trigger a dependency installation/redeployment.

## Release checklist

- [ ] Deployment completes successfully.
- [ ] Public URL opens in a private browser window.
- [ ] All smoke tests above pass.
- [ ] Public URL is added to the README and repository About website field.
- [ ] README includes a deployment badge after the final app URL is known.
- [ ] A versioned GitHub release is prepared after deployment verification.
