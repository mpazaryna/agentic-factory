# App Store Submission

Comprehensive checklist for App Store Review Guidelines compliance.

## Pre-Submission Checklist

### Critical (Will Reject)

- [ ] **No crashes** - App runs without crashing
- [ ] **No placeholder content** - All content is final
- [ ] **No broken links** - All URLs work
- [ ] **No incomplete features** - Everything works or is hidden
- [ ] **Privacy policy** - Accessible and accurate
- [ ] **Usage strings** - All permissions have descriptions in Info.plist

### High Priority (Likely Reject)

- [ ] **Accurate metadata** - Screenshots match actual app
- [ ] **Restore purchases** - Works for IAP apps
- [ ] **Sign in with Apple** - Required if using third-party login
- [ ] **Age rating** - Matches actual content
- [ ] **No private APIs** - Only public Apple APIs used

## App Store Review Guidelines Summary

### 1. Safety

| Guideline | Requirement |
|-----------|-------------|
| 1.1 Objectionable Content | No offensive, insensitive, upsetting content |
| 1.2 User Generated Content | Filtering, reporting, blocking required |
| 1.3 Kids Category | Extra privacy protections, no ads |
| 1.4 Physical Harm | No dangerous activities |
| 1.5 Developer Info | Accurate contact information |

### 2. Performance

| Guideline | Requirement |
|-----------|-------------|
| 2.1 App Completeness | Fully functional, no placeholders |
| 2.2 Beta/Demo | No beta or demo labels |
| 2.3 Accurate Metadata | Screenshots and descriptions match |
| 2.4 Hardware Compatibility | Works on claimed devices |
| 2.5 Software Requirements | Minimum iOS version accurate |

### 3. Business

| Guideline | Requirement |
|-----------|-------------|
| 3.1 Payments | Use Apple's IAP for digital goods |
| 3.1.1 In-App Purchase | Clear pricing, restore purchases |
| 3.1.2 Subscriptions | Clear terms, easy cancellation info |
| 3.2 Other Business | No manipulation of reviews |

### 4. Design

| Guideline | Requirement |
|-----------|-------------|
| 4.1 Copycats | Original design, no clones |
| 4.2 Minimum Functionality | More than a simple website |
| 4.3 Spam | Unique app, not duplicate |
| 4.4 Extensions | Must include app functionality |
| 4.5 Apple Sites | No scraping Apple services |

### 5. Legal

| Guideline | Requirement |
|-----------|-------------|
| 5.1 Privacy | Accurate privacy declarations |
| 5.1.1 Data Collection | Disclose all data collected |
| 5.1.2 Data Use | Clear purpose for data |
| 5.2 Intellectual Property | No trademark infringement |
| 5.3 Gaming/Gambling | Proper licensing required |

## Info.plist Requirements

### Privacy Usage Strings

```xml
<!-- Camera -->
<key>NSCameraUsageDescription</key>
<string>We need camera access to take profile photos</string>

<!-- Photo Library -->
<key>NSPhotoLibraryUsageDescription</key>
<string>We need photo access to let you choose a profile picture</string>

<!-- Location -->
<key>NSLocationWhenInUseUsageDescription</key>
<string>We use your location to show nearby restaurants</string>

<!-- Microphone -->
<key>NSMicrophoneUsageDescription</key>
<string>We need microphone access for voice messages</string>

<!-- Contacts -->
<key>NSContactsUsageDescription</key>
<string>We use contacts to help you find friends</string>

<!-- Bluetooth -->
<key>NSBluetoothAlwaysUsageDescription</key>
<string>We use Bluetooth to connect to your devices</string>
```

### Required Keys

```xml
<!-- App Transport Security (if using HTTP) -->
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSExceptionDomains</key>
    <dict>
        <!-- Specific exceptions only -->
    </dict>
</dict>

<!-- Background Modes (if used) -->
<key>UIBackgroundModes</key>
<array>
    <string>audio</string>
    <string>location</string>
</array>
```

## App Store Connect Metadata

### App Information

- [ ] **App Name** (30 characters) - Clear, unique
- [ ] **Subtitle** (30 characters) - Descriptive
- [ ] **Category** - Primary and secondary
- [ ] **Age Rating** - Complete questionnaire accurately
- [ ] **Privacy Policy URL** - Valid, accessible link

### Version Information

- [ ] **What's New** - Describe changes for updates
- [ ] **Description** (4000 characters) - Features, not marketing fluff
- [ ] **Keywords** (100 characters) - Relevant, no competitors
- [ ] **Support URL** - Working help page
- [ ] **Marketing URL** - Optional but recommended

### Screenshots

| Device | Required Sizes |
|--------|---------------|
| iPhone 6.7" | 1290 x 2796 |
| iPhone 6.5" | 1242 x 2688 |
| iPhone 5.5" | 1242 x 2208 |
| iPad 12.9" | 2048 x 2732 |

- [ ] At least 3 screenshots per device
- [ ] Show actual app UI (not marketing graphics only)
- [ ] Text localized if app is localized

## Common Rejection Reasons

### 1. Guideline 2.1 - App Completeness
**Problem**: Placeholder content, broken features, "coming soon"
**Fix**: Remove or hide incomplete features

### 2. Guideline 2.3 - Accurate Metadata
**Problem**: Screenshots don't match app
**Fix**: Update screenshots to current UI

### 3. Guideline 3.1.1 - In-App Purchase
**Problem**: No restore purchases button
**Fix**: Add visible restore functionality

### 4. Guideline 5.1.1 - Data Collection
**Problem**: Privacy declarations don't match actual collection
**Fix**: Audit all data collection and update declarations

### 5. Guideline 4.2 - Minimum Functionality
**Problem**: App is too simple or just a web wrapper
**Fix**: Add native features and functionality

## Testing Before Submission

### Device Testing
- [ ] Test on oldest supported iOS version
- [ ] Test on smallest supported device
- [ ] Test on largest supported device
- [ ] Test on iPad (if universal)

### Scenario Testing
- [ ] Fresh install (no existing data)
- [ ] Upgrade from previous version
- [ ] Offline/poor connectivity
- [ ] Permissions denied
- [ ] Low storage
- [ ] Background/foreground cycling

### Account Testing
- [ ] New user signup
- [ ] Existing user login
- [ ] Logout and re-login
- [ ] Delete account (if applicable)
- [ ] Restore purchases (if IAP)
