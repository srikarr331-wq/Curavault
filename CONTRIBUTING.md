# Contributing to CuraVault

Thank you for your interest in contributing to CuraVault! This document provides guidelines and instructions for contributing.

## Code of Conduct

We are committed to providing a welcoming and inspiring community. Please read and adhere to our Code of Conduct in all interactions.

## Getting Started

### Prerequisites
- Python 3.11+
- Node.js 18+
- PostgreSQL 15+
- Redis 7+
- Git

### Development Setup

1. **Fork the Repository**
```bash
git clone https://github.com/srikarr331-wq/curavault.git
cd curavault
```

2. **Create a Feature Branch**
```bash
git checkout -b feature/your-feature-name
```

3. **Backend Development**
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Configure .env as needed
python main.py
```

4. **Frontend Development**
```bash
cd frontend
npm install
npm run dev
```

## Development Workflow

### Before You Start
- Check [Issues](https://github.com/srikarr331-wq/curavault/issues) for existing work
- Create an issue if one doesn't exist
- Discuss major changes in an issue before implementing

### Code Standards

#### Python (Backend)
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use type hints for function signatures
- Maximum line length: 100 characters
- Use meaningful variable names
- Document public functions with docstrings

```python
def authenticate_user(email: str, password: str) -> User:
    """
    Authenticate user with email and password.

    Args:
        email: User email address
        password: User password

    Returns:
        User object if authentication successful

    Raises:
        InvalidCredentials: If email or password is incorrect
    """
    pass
```

#### TypeScript/React (Frontend)
- Follow [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript)
- Use functional components with hooks
- Props should be properly typed
- Maximum line length: 100 characters
- Use meaningful component names

```typescript
interface UserProfileProps {
  userId: string;
  onUpdate?: (user: User) => void;
}

export const UserProfile: React.FC<UserProfileProps> = ({
  userId,
  onUpdate,
}) => {
  // Component implementation
};
```

### Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/) format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Code style (formatting, etc.)
- `refactor`: Code refactoring
- `perf`: Performance improvement
- `test`: Test addition/modification
- `chore`: Build, dependencies, etc.

**Examples**:
```
feat(auth): add two-factor authentication
fix(reports): resolve file upload timeout issue
docs(api): update endpoint documentation
test(profile): add patient profile tests
```

### Testing Requirements

#### Backend Tests
```bash
cd backend
pytest --cov=app --cov-report=html
```

#### Frontend Tests
```bash
cd frontend
npm run test
```

**Requirements**:
- Minimum 80% code coverage
- All public functions must have tests
- Test names should be descriptive
- Use fixtures for setup/teardown

### Pull Request Process

1. **Update Your Branch**
```bash
git fetch origin
git rebase origin/main
```

2. **Run Tests Locally**
```bash
# Backend
cd backend && pytest

# Frontend
cd frontend && npm run test
```

3. **Push Changes**
```bash
git push origin feature/your-feature-name
```

4. **Create Pull Request**
   - Use descriptive title
   - Reference related issues (#123)
   - Provide clear description of changes
   - Include screenshots for UI changes
   - List any breaking changes

**PR Template**:
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Related Issues
Fixes #123

## Testing
Describe how changes were tested

## Screenshots (if applicable)
Add screenshots for UI changes

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex logic
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] All tests passing
- [ ] No new warnings generated
```

## Documentation

### Code Documentation
- Use clear, concise comments
- Document complex algorithms
- Include examples for public APIs
- Update README for significant features

### API Documentation
- Document all endpoints
- Include request/response examples
- List error codes and meanings
- Note authentication requirements

### Architecture Documentation
- Diagram key components
- Explain design decisions
- Document data flows
- Include sequence diagrams

## Security Considerations

When contributing security-related code:
- Never commit secrets or credentials
- Use environment variables for configuration
- Follow OWASP guidelines
- Add security tests
- Document security implications
- Consider edge cases and attacks

## Performance Guidelines

- Profile code before optimizing
- Use appropriate data structures
- Implement caching where beneficial
- Minimize database queries
- Optimize file operations
- Document performance considerations

## Git Workflow

```bash
# Create and switch to feature branch
git checkout -b feature/your-feature

# Make changes and commit
git add .
git commit -m "feat(scope): description"

# Keep branch updated
git fetch origin
git rebase origin/main

# Push changes
git push origin feature/your-feature

# Create pull request via GitHub
```

## Review Process

### Code Review Criteria
- Code quality and standards
- Test coverage
- Documentation
- Security implications
- Performance impact
- Breaking changes

### Feedback and Iteration
- Respond to reviewer comments
- Request re-review after changes
- Be respectful and professional
- Ask questions if unclear

## Release Process

- Versions follow [Semantic Versioning](https://semver.org/)
- CHANGELOG.md maintained
- Tags created for releases
- Release notes published

## Getting Help

- **Questions**: Create a discussion or issue
- **Documentation**: Check docs/ folder
- **Examples**: Review test cases
- **Community**: Engage with other contributors

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- GitHub acknowledgments

## Questions?

- Check existing documentation
- Search closed issues
- Ask in a new issue
- Start a discussion

Thank you for contributing to CuraVault! 🙏