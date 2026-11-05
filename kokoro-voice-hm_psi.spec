Name:		kokoro-voice-hm_psi
Version:	1.0
Release:	1
Summary:	Hindi male Kokoro voice hm_psi
URL:		https://huggingface.co/hexgrad/Kokoro-82M/tree/main/voices
License:	Apache-2.0
BuildArch:	noarch
Group:		System/Multimedia
Provides:	kokoro-voice
Provides:	kokoro-voice-hi
Requires:	kokoro-model >= 1.0

%sourcelist
https://huggingface.co/hexgrad/Kokoro-82M/resolve/main/voices/hm_psi.pt

%description
%{summary}.
Uses the shared checkpoint in kokoro-model.
Pronunciation uses espeak-ng.
Select it with: kokoro -m hm_psi

%install
mkdir -p %{buildroot}%{_datadir}/kokoro/voices
install -c -m 644 %{S:0} %{buildroot}%{_datadir}/kokoro/voices/hm_psi.pt

%files
%{_datadir}/kokoro/voices/hm_psi.pt
